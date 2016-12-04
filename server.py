import socket
from client import Client, GameState
#from gamestate import GameState

IP_LOCAL = "192.168.1.72" # Local here is mikes MACBOOK
IP_SERVER = "138.68.66.77"
UDP_IP = IP_SERVER

UDP_PORT = 9876

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# All the connecting clients will be held in this array
clients = list()

print "Server up n runnin..."
while True:
    print("Waiting for client data...")
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("Handling client...")

    #ip = addr[0]
    #port = addr[1]
    client = Client(addr, data)
    foundClient = False
    for c in clients:
        c.currentGameState = client.currentGameState
        if c.clientId == client.clientId:
            foundClient = True

    # Adding new client that just "connected"
    if foundClient is False:
        clients.append(client)

    # Printing some relevant info about clients
    for index, client in enumerate(clients):
        print("Client ", index, " info:")
        print(client.clientId)
        print(client.ip)
        print(client.port)
        print("(x: ", client.currentGameState.x, "y: ", client.currentGameState.y, ")")


    #sock.sendto("THIS IS A MESSAGE FROM SPARTA", (clients[0].ip, 61991))
    for index, client in enumerate(clients):
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        clientIp = client.ip
        sock.sendto(client.currentGameState.getGameStateAsString(), (clientIp, 61991))
