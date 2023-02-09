# functions for the connect-4 game

# This series of lists act as the game board where 0 means no token, 1 equals player1 token and 2 means player2 token
col0 = [0, 0, 0, 0, 0]
col1 = [0, 0, 0, 0, 0]
col2 = [0, 0, 0, 0, 0]
col3 = [0, 0, 0, 0, 0]
col4 = [0, 0, 0, 0, 0]
cols = [col0, col1, col2, col3, col4]





def updateRows():
    global row0
    global row1
    global row2
    global row3
    global row4
    row0 = [col0[4], col1[4], col2[4], col3[4], col4[4]]
    row1 = [col0[3], col1[3], col2[3], col3[3], col4[3]]
    row2 = [col0[2], col1[2], col2[2], col3[2], col4[2]]
    row3 = [col0[1], col1[1], col2[1], col3[1], col4[1]]
    row4 = [col0[0], col1[0], col2[0], col3[0], col4[0]]
    global rows
    rows = [row0, row1, row2, row3, row4]



def init():
    print("Welcome to connect 4!!")
    print("This game consists on getting 4 of your tokens in a row.")
    print("First lets create the players")
    definePlayers()
    createBoard()
    updateLoop()

def definePlayers():
    global player1
    player1 = input("Select the name of player 1: ")
    player1token = "X"
    print(player1, " will be using X")
    global player2
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

def selectColPlayer1():
    c = 1
    while c == 1:
        col = int(input("Player1: Select the column to drop the token: "))
        if col >= 1 and col <= 5:
            return int(col)
            c = 0
        else:
            print("Incorrect value. Select a number between 1 and 5.")

def selectColPlayer2():
    c = 1
    while c == 1:
        col = int(input("Player2: Select the column to drop the token: "))
        if col >= 1 and col <= 5:
            return int(col)
            c = 0
        else:
            print("Incorrect value. Select a number between 1 and 5.")

def printUpdateBoard():
    print("   1  2  3  4  5    ")
    print(" ", end="")
    for celda in row0:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("")

    print(" ", end="")
    for celda in row1:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("")

    print(" ", end="")
    for celda in row2:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")

    print("")

    print(" ", end="")
    for celda in row3:
        if celda == 0:
            print("| ", end=" ")
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("")

    print(" ", end="")
    for celda in row4:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("")


def updateLoop():
    updateRows()
    g = 1
    while g == 1:
        col = selectColPlayer1()

        # match statement for the selection of player 1.
        match col:
            case 1:
                for i in range(len(col0)):
                    if col0[i] == 0:
                        col0[i] = 1
                        break
            case 2:
                for i in range(len(col1)):
                    if col1[i] == 0:
                        col1[i] = 1
                        break
            case 3:
                for i in range(len(col2)):
                    if col2[i] == 0:
                        col2[i] = 1
                        break
            case 4:
                for i in range(len(col3)):
                    if col3[i] == 0:
                        col3[i] = 1
                        break
            case 5:
                for i in range(len(col4)):
                    if col4[i] == 0:
                        col4[i] = 1
                        break
        updateRows()
        printUpdateBoard()
        g = check4Horizontal()
        if g == 0:
            break
        g = check4Vertical()
        if g == 0:
            break
        col = selectColPlayer2()

        match col:
            case 1:
                for i in range(len(col0)):
                    if col0[i] == 0:
                        col0[i] = 2
                        break
            case 2:
                for i in range(len(col1)):
                    if col1[i] == 0:
                        col1[i] = 2
                        break
            case 3:
                for i in range(len(col2)):
                    if col2[i] == 0:
                        col2[i] = 2
                        break
            case 4:
                for i in range(len(col3)):
                    if col3[i] == 0:
                        col3[i] = 2
                        break
            case 5:
                for i in range(len(col4)):
                    if col4[i] == 0:
                        col4[i] = 2
                        break
        updateRows()
        printUpdateBoard()
        g = check4Horizontal()
        if g == 0:
            break
        g = check4Vertical()


def check4Horizontal():
    for i in range(len(cols)):
        for j in range(len(rows)):
            if rows[i][j] == 1 and rows[i][j + 1] == 1 and rows[i][j + 2] == 1 and rows[i][j + 3] == 1:
                print("Player ", player1, " won!")
                return 0
            if rows[i][j] == 2 and rows[i][j + 1] == 2 and rows[i][j + 2] == 2 and rows[i][j + 3] == 2:
                print("Player ", player2, " won!")
                return 0
    return 1

def check4Vertical():
    for i in range(len(rows)):
        for j in range(len(cols)):
            if cols[i][j] == 1 and cols[i][j + 1] == 1 and cols[i][j + 2] == 1 and cols[i][j + 3] == 1:
                print("Player ", player1, " won!")
                return 0
            if cols[i][j] == 2 and cols[i][j + 1] == 2 and cols[i][j + 2] == 2 and cols[i][j + 3] == 2:
                print("Player ", player2, " won!")
                return 0
    return 1



