import socket
from client import Client

UDP_IP = "138.68.66.77" 
UDP_PORT = 9876

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

clients = []

print "Server up n runnin..."
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Addr: ", addr
    print "received message:", data
