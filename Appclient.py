import socket
import argparse

def parse_input_argument():
    parser = argparse.ArgumentParser(description='This is a client program that create a tunnel\
                                                  to the server over various TCP connections.')

    parser.add_argument('-s', '--server', required=True,
                    help="The IP address and (TCP) port number of the tunnel server.\
                               The format is 'server ip:server port'.")

args = parse_input_argument()
    
tcp_server_ip = args.server.split(':')[0]
tcp_server_port = int(args.server.split(':')[1])

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.connect((tcp_server_ip, tcp_server_port))

count = 0
while True:
    count += 1
    sock.send(f"sending app client port {tcp_server_port} {count}".encode())
    print(f"sending test port {tcp_server_port} {count}".encode())
    res = sock.recv(1024)
    print(f"recieving app client port {res.decode}".encode())
    