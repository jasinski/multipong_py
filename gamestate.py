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
