# functions for the connect 4 game
row0 = list(range(0, 6))
row1 = list(range(0, 6))
row2 = list(range(0, 6))
row3 = list(range(0, 6))
row4 = list(range(0, 6))



def init():
    print("Welcome to connect 4!!")
    print("This game consists on getting 4 of your tokens in a row.")
    print("First lets create the players")

def definePlayers():
    player1 = input("Select the name of player 1: ")
    player1token = "X"
    print(player1, " will be using X")
    player2 = input("Select the name of player 2: ")
    player2token = "0"
    print(player2, " will be using 0")

def createBoard():
    print("  |  |  |  |  |  |  |  ") # Row 4
    print("  |  |  |  |  |  |  |  ") # Row 3
    print("  |  |  |  |  |  |  |  ") # Row 2
    print("  |  |  |  |  |  |  |  ") # Row 1
    print("  |  |  |  |  |  |  |  ") # Row 0

def selectRowPlayer1():
    col = input("PLayer1: Select the column to drop the token: ")
    return int(col)

def selectRowPlayer2():
    col = input("Player2: Select the column to drop the token: ")
    return int(col)

def updateLoop(colSel):
    return 0