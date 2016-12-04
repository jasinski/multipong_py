class Client:

    def __init__(self, clientId, ip, port):
        print("init 1 is used")
        self.clientId = clientId
        self.ip = ip
        self.port = int(port)

    def __init__(self, address, data):
        print("init 2 is used")
        self.ip = address[0]
        self.port = int(address[1])
        arr = self.dataStringToArray(data)
        self.clientId = arr[0]
        self.msgType = arr[1]
        self.currentGameState = GameState(self.clientId, arr[2])

    def dataStringToArray(self, data):
        return data.split(":")

class GameState:

    def __init__(self, parentId, x, y):
        self.parentId = parentId
        self.x = x
        self.y = y

    def __init__(self, parentId, gameStateString):
        self.parentId = parentId
        print "gameStateString:", gameStateString
        arr = gameStateString.split(",")
        self.x = arr[0]
        self.y = arr[1]

    def getGameStateAsString(self):
        return self.parentId + "," + self.x + "," + self.y
