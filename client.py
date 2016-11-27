class Client:

    def __init__(self, clientId, ip, port):
        self.clientId = clientId
        self.ip = ip
        self.port = port

    def __init__(self, address, data):
        self.ip = address[0]
        self.port = address[0]
        arr = self.dataStringToArray(data)
        self.clientId = arr[0]
        self.msgType = arr[1]
        self.currentGameState = GameState(arr[2])

    def dataStringToArray(self, data):
        return data.split(":")

class GameState:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, gameStateString):
        print "gameStateString:", gameStateString
        arr = gameStateString.split(",")
        self.x = arr[0]
        self.y = arr[1]
