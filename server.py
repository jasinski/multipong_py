import socket
from client import Client, GameState

UDP_IP = "138.68.66.77"
UDP_PORT = 9876

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

clients = list()

print "Server up n runnin..."
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    #ip = addr[0]
    #port = addr[1]
    client = Client(addr, data)
    foundClient = False
    for c in clients:
        if c.clientId == client.clientId:
            c.currentGameState = client.currentGameState
            foundClient = True

    if foundClient is False:
        clients.append(client)


    for index, client in enumerate(clients):
        print("Client ", index, " info:")
        print(client.clientId)
        print(client.ip)
        print(client.port)
        print("(x: ", client.currentGameState.x, "y: ", client.currentGameState.y, ")")
