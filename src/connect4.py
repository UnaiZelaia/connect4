# functions for the connect-4 game

# This series of lists act as the game board where 0 means no token, 1 equals player1 token and 2 means player2 token
col0 = [0, 0, 0, 0, 0]
col1 = [0, 0, 0, 0, 0]
col2 = [0, 0, 0, 0, 0]
col3 = [0, 0, 0, 0, 0]
col4 = [0, 0, 0, 0, 0]

row0 = [col0[0], col1[0], col2[0], col3[0], col4[0]]
row1 = [col0[1], col1[1], col2[1], col3[1], col4[1]]
row2 = [col0[2], col1[2], col2[2], col3[2], col4[2]]
row3 = [col0[3], col1[3], col2[3], col3[3], col4[3]]
row4 = [col0[4], col1[4], col2[4], col3[4], col4[4]]



def init():
    print("Welcome to connect 4!!")
    print("This game consists on getting 4 of your tokens in a row.")
    print("First lets create the players")
    definePlayers()
    createBoard()
    updateLoop()

def definePlayers():
    player1 = input("Select the name of player 1: ")
    player1token = "X"
    print(player1, " will be using X")
    player2 = input("Select the name of player 2: ")
    player2token = "0"
    print(player2, " will be using 0")

def createBoard():
    print("   1 2 3 4 5    ")  # Column numbers
    print("  | | | | | |  ")  # Row 4
    print("  | | | | | |  ")  # Row 3
    print("  | | | | | |  ")  # Row 2
    print("  | | | | | |  ")  # Row 1
    print("  | | | | | |  ")  # Row 0

def selectRowPlayer1():
    col = input("Player1: Select the column to drop the token: ")
    return int(col)

def selectRowPlayer2():
    col = input("Player2: Select the column to drop the token: ")
    return int(col)

def printUpdateBoard():
    print("   1  2  3  4  5    ")
    for celda in row0:
        if celda == 0:
            print("| |", end=" ");
        if celda == 1:
            print("|X|", end=" ")
        if celda == 2:
            print("|O|", end=" ")
    print("")


    for celda in row1:
        if celda == 0:
            print("| |", end=" ");
        if celda == 1:
            print("|X|", end=" ")
        if celda == 2:
            print("|O|", end=" ")
    print("")


    for celda in row2:
        if celda == 0:
            print("| |", end=" ");
        if celda == 1:
            print("|X|", end=" ")
        if celda == 2:
            print("|O|", end=" ")

    print("")

    for celda in row3:
        if celda == 0:
            print("| |", end=" ");
        if celda == 1:
            print("|X|", end=" ")
        if celda == 2:
            print("|O|", end=" ")

    print("")


    for celda in row4:
        if celda == 0:
            print("| |", end=" ");
        if celda == 1:
            print("|X|", end=" ")
        if celda == 2:
            print("|O|", end=" ")
    print("")


def updateLoop():
    g = 1
    while g == 1:
        col = selectRowPlayer1()

        # match statement for the selection of player 1.
        match col:
            case 1:
                for space in col0:
                    if space == 0:
                        col0[space] = 1
            case 2:
                for space in col1:
                    if space == 0:
                        col1[space] = 1
            case 3:
                for space in col2:
                    if space == 0:
                        col2[space] = 1
            case 4:
                for space in col3:
                    if space == 0:
                        col3[space] = 1
            case 5:
                for space in col4:
                    if space == 0:
                        col4[space] = 1

        col = selectRowPlayer2()

        match col:
            case 1:
                for space in col0:
                    if space == 0:
                        col0[space] = 2
                        1
            case 2:
                for space in col1:
                    if space == 0:
                        col1[space] = 2
            case 3:
                for space in col2:
                    if space == 0:
                        col2[space] = 2
            case 4:
                for space in col3:
                    if space == 0:
                        col3[space] = 2
            case 5:
                for space in col4:
                    if space == 0:
                        col4[space] = 2

        printUpdateBoard()



