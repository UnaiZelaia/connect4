import datetime

# functions for the connect4 game
# This file contains all the functions necessary for the game to execute.
# the init() function should be called in a main file for the game to start executing

# This series of lists act as the game board where 0 means no token, 1 equals player1 token and 2 means player2 token
col0 = [0, 0, 0, 0, 0]
col1 = [0, 0, 0, 0, 0]
col2 = [0, 0, 0, 0, 0]
col3 = [0, 0, 0, 0, 0]
col4 = [0, 0, 0, 0, 0]

# List of lists that contains all of the columns
cols = [col0, col1, col2, col3, col4]

def updateRows():
    # This function updates the rows lists with the information from the column lists.
    # This is needed here and not in the columns because the player input is directly entered into the column variables
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

    # List of lists that contains all of the rows
    global rows
    rows = [row0, row1, row2, row3, row4]


def init():
    # This function initializes the game by calling 3 functions.
    # The first 2 functions are executed only once and the third function is looped through until the end of the game.
    print("Welcome to connect 4!!")
    print("This game consists on getting 4 of your tokens in a row.")
    print("First lets create the players")

    definePlayers()
    createBoard()
    updateLoop()


def definePlayers():
    # This function will initialize the player variables as globals
    # and then take player input for the name of the players.
    # It also defines the player tokens.
    global player1
    player1 = input("Select the name of player 1: ")
    player1token = "X"
    print(player1, " will be using X")

    global player2
    player2 = input("Select the name of player 2: ")
    player2token = "0"
    print(player2, " will be using 0")


def createBoard():
    # This function prints out a blank board so it will executed at the start of the game.
    print("   1 2 3 4 5    ")  # Column numbers
    print("  | | | | | |  ")  # Row 4
    print("  | | | | | |  ")  # Row 3
    print("  | | | | | |  ")  # Row 2
    print("  | | | | | |  ")  # Row 1
    print("  | | | | | |  ")  # Row 0


def selectColPlayer1():
    # This function takes input for the column where player 1 wants to drop the token.
    # The input is controlled so the user can only input
    c = 1
    while c == 1:
        try:
            col = int(input("Player1: Select the column to drop the token: "))
        except:
            continue
        if 1 <= col <= 5: # Check if the input is between 1 and 5.
            if cols[col - 1][4] == 0:  # Check if the column the user selected has an available space in the last (top) position.
                return int(col)
            else:
                print("This column is full! Try another one.")
        else:
            print("Incorrect value. Select a number between 1 and 5.")


def selectColPlayer2():
    # This function behaves the same as the one for player 1 but for player2
    c = 1
    while c == 1:
        col = int(input("Player2: Select the column to drop the token: "))
        if 1 <= col <= 5:
            if cols[col - 1][4] == 0:
                return int(col)
                c = 0
            else:
                print("This column is full! Try another one.")
        else:
            print("Incorrect value. Select a number between 1 and 5.")




def printUpdateBoard():
    # This function prints out a board with the information stored in the rows lists.
    # If the list contains 0 in the position, the cell will be empty
    # If it contains 1, the cell will have an X, the player 1 token.
    # If it contains 2, the cell will have an O, the player 2 token.

    print("   1  2  3  4  5    ")
    print(" ", end="")
    for celda in row0:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("|")

    print(" ", end="")
    for celda in row1:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("|")

    print(" ", end="")
    for celda in row2:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")

    print("|")

    print(" ", end="")
    for celda in row3:
        if celda == 0:
            print("| ", end=" ")
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("|")

    print(" ", end="")
    for celda in row4:
        if celda == 0:
            print("| ", end=" ");
        if celda == 1:
            print("|X", end=" ")
        if celda == 2:
            print("|O", end=" ")
    print("|")



def updateLoop():
    # This function is the main update loop for the game.
    # Several functions are called from this to form the game loop.

    # First we declare a variable and use it for the while loop.
    g = 1
    while g == 1:
        # First the player 1 will select a column to drop the token.
        col = selectColPlayer1()

        # match statement for the selection of player 1.
        # This will change the column position where the col[] variable is 0 (not used) to 1 (used by player 1)
        match col:
            case 1:
                for i in range(len(col0)):
                    if col0[i] == 0:  # Check if the position of the column is blank.
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
        # After the selection and updating of the column, the rows are updated with the new information from the columns.
        updateRows()

        # The board with the new information is printed out
        printUpdateBoard()


        # And the game checks for win condition in a vertical, horizontal and diagonal way.
        # The win checkers return 1 if the win condition is not met and 0 if it is.
        g = check4Horizontal()
        if g == 0:
            winner = player1
            writeToFile(winner)
            break
        g = check4Vertical()
        if g == 0:
            winner = player1
            writeToFile(winner)
            break
        g = checkDiagonal1()
        if g == 0:
            winner = player1
            writeToFile(winner)
            break
        g = checkDiagonal2()
        if g == 0:
            winner = player1
            writeToFile(winner)
            break
        g = checkEndGame()
        if g == 0:
            break

        # Then the process is repeated for player 2
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
        # There is no need for break statements in the player 2 win checks since they are at the end of the loop.
        g = check4Horizontal()
        if g == 0:
            winner = player2
            writeToFile(winner)
            break
        g = check4Vertical()
        if g == 0:
            winner = player2
            writeToFile(winner)
            break
        g = checkDiagonal1()
        if g == 0:
            winner = player2
            writeToFile(winner)
            break
        g = checkDiagonal2()
        if g == 0:
            winner = player2
            writeToFile(winner)
            break
        g = checkEndGame()



def check4Horizontal():
    # This function checks for win condition in an horizontal way

    # This structure loops through the rows and columns of our board in search of 4 token in a row
    # After the loop, there are 2 if structures that check the win condition for player 1 and 2.
    for i in range(len(cols)):
        for j in range(len(rows)):
            try:
                # Win condition for player 1
                # Doing +1 in the j variable checks the same row 1 position to the right.
                # We can do this up to +3 to check for 4
                if rows[i][j] == 1 and rows[i][j + 1] == 1 and rows[i][j + 2] == 1 and rows[i][j + 3] == 1:
                    print("Player ", player1, " won!")
                    return 0
            except:
                # This exception allows for control of the list out of index exception
                # Originally, if the user input the column 5 to drop the token, the first expression of the
                # win condition structure would resolve to true, but would throw an exception in the next one
                # because of the +1.
                if rows[i] == 4 and rows[j] == 4:
                    # The exception will only return 1 (win condition not met) as long as the position of the
                    # loop is the last one available.
                    # else it will continue executing despite the exceptions.
                    return 1
                else:
                    continue
            try:
                # Same structure as above but for player 2
                if rows[i][j] == 2 and rows[i][j + 1] == 2 and rows[i][j + 2] == 2 and rows[i][j + 3] == 2:
                    print("Player ", player2, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue
    return 1


def check4Vertical():
    # In the vertical win condition, the same happens but the rows and cols variables are inverted.
    # Therefore, the j+1 expression will check the cell above, instead of the one on the right.
    # The rest is the same as in the Horizontal win checker.
    for i in range(len(rows)):
        for j in range(len(cols)):
            try:
                if cols[i][j] == 1 and cols[i][j + 1] == 1 and cols[i][j + 2] == 1 and cols[i][j + 3] == 1:
                    print("Player ", player1, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue

            try:
                if cols[i][j] == 2 and cols[i][j + 1] == 2 and cols[i][j + 2] == 2 and cols[i][j + 3] == 2:
                    print("Player ", player2, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue
    return 1


def checkDiagonal1():
    # This function checks for the diagonal win condition.

    # It is the same structure as the other win checkers but in this one the variables are checked in a row +1
    # and col + 1 way. This mean that it will check for 4 tokens in row one above and one to the right.
    for i in range(len(rows)):
        for j in range(len(cols)):
            try:
                if cols[i][j] == 1 and cols[i + 1][j + 1] == 1 and cols[i + 2][j + 2] == 1 and cols[i + 3][j + 3] == 1:
                    print("Player ", player1, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue

            try:
                if cols[i][j] == 2 and cols[i + 1][j + 1] == 2 and cols[i + 2][j + 2] == 2 and cols[i + 3][j + 3] == 2:
                    print("Player ", player2, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue
    return 1


def checkDiagonal2():
    # This function checks for the inverse diagonal win condition.

    # It is the same structure as the other win checkers but in this one the variables are checked in a row -1
    # and col + 1 way. This mean that it will check for 4 tokens in row one below and one to the right.

    for i in range(len(rows)):
        for j in range(len(cols)):
            try:
                if cols[i][j] == 1 and cols[i - 1][j + 1] == 1 and cols[i - 2][j + 2] == 1 and cols[i - 3][j + 3] == 1:
                    print("Player ", player1, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue

            try:
                if cols[i][j] == 2 and cols[i - 1][j + 1] == 2 and cols[i - 2][j + 2] == 2 and cols[i - 3][j + 3] == 2:
                    print("Player ", player2, " won!")
                    return 0
            except:
                if rows[i] == 4 and rows[j] == 4:
                    return 1
                else:
                    continue
    return 1



def checkEndGame():
    # This function checks if all the columns are full (they have 1 or 2 in all the cells)
    # This is done with 2 nested loops that check every cell for every column list.
    count = 0
    i = 0
    fullCols = 0
    for col in cols:
        for celda in col:
            if celda != 0:
                count += 1
            if count == 5:
                fullCols += 1
                count = 0
            if fullCols == 5:
                print("There are no more cells left. It's a draw.")
                return 0
            else:
                return 1

def writeToFile(winner):
    file = open("../files/connect4.txt", "a+")
    file.write(boardStateString(winner))
    file.write
    file.close()



def boardStateString(winner):
    # This function prints out a board with the information stored in the rows lists.
    # If the list contains 0 in the position, the cell will be empty
    # If it contains 1, the cell will have an X, the player 1 token.
    # If it contains 2, the cell will have an O, the player 2 token.
    board = ""

    board += "  1  2  3  4  5\n"
    board += " "
    for celda in row0:
        if celda == 0:
            board += "|  "
        if celda == 1:
            board += "|X "
        if celda == 2:
            board += "|O "
    board += "|\n"

    board += " "
    for celda in row1:
        if celda == 0:
            board += "|  "
        if celda == 1:
            board += "|X "
        if celda == 2:
            board += "|O "
    board += "|\n"

    board += " "
    for celda in row2:
        if celda == 0:
            board += "|  "
        if celda == 1:
            board += "|X "
        if celda == 2:
            board += "|O "
    board += "|\n"

    board += " "
    for celda in row3:
        if celda == 0:
            board += "|  "
        if celda == 1:
            board += "|X "
        if celda == 2:
            board += "|O "
    board += "|\n"

    board += " "
    for celda in row4:
        if celda == 0:
            board += "|  "
        if celda == 1:
            board += "|X "
        if celda == 2:
            board += "|O "
    board += "|\n\n\n"
    board += "This game was played between " + player1 + " and " + player2 +".\n"
    data = datetime.datetime.now()
    board += "The game was played at " + data.strftime("%d-%m-%Y") + " at " + data.strftime("%H:%M") + "\n"
    board += "The winner of the game was: " + winner
    board += "\n============================================================================"
    board += "\n\n"

    return board



