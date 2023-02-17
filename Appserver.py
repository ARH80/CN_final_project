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
    
tcp_server_ip = args.server.split(':')[0]
tcp_server_port = int(args.server.split(':')[1])

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((tcp_server_ip, tcp_server_port))

count = 0

while True:
    count += 1
    msg, address = sock.recvfrom(1024)
    print(f"App server recieved from {address} msg: {msg}")
    sock.sendto(f"app server from port {tcp_server_port} sends {count}".encode(), address)
    
