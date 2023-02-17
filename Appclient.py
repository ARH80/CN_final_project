import socket
import argparse

def parse_input_argument():
    parser = argparse.ArgumentParser(description='This is a client program that create a tunnel\
                                                  to the server over various TCP connections.')

    parser.add_argument('-s', '--server', required=True,
                    help="The IP address and (TCP) port number of the tunnel server.\
                               The format is 'server ip:server port'.")
    args = parser.parse_args()
    return args

args = parse_input_argument()
    
udpserver_ip = args.server.split(':')[0]
udpserver_port = int(args.server.split(':')[1])

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

count = 0
while True:
    count += 1
    sock.sendto(f"sending app client port {udpserver_port} {count}".encode(), (udpserver_ip, udpserver_port))
    print(f"sending test port {udpserver_port} {count}".encode())
    res = sock.recv(1024)
    print(f"recieving app client port {res.decode}".encode())
    