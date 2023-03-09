import time;
loading=["Your game is loading...",3,2,1]
count = 0
answer1="mercury"
answer2="1,6"
answer3="amazonas"
answer4="scotland"
answer5="jupiter"


def menu():

    print("*================================*")
    print("Welcome to GuesstheWord game")
    for n in loading:
        print(n)
        time.sleep(0.7)
    firstquestion(count)
    finish(count)
def firstquestion(count):
    
    first = input("What is the closest planet to the earth ?\n")

    if first == answer1:
        print("The answer is correct\n")
        count = count + 1
        secondquestion(count)

    else:
        print("Hint:Old thermometers had it\n ")
        first = input("What is the closest planet to the sun?\n")
    if (first == answer1):
        print("The answer is correct\n")

        count = count + 1
        secondquestion(count)
    else:
        print("Hint:Starts with the letter M\n")
        first = input("What is the closest planet to the sun?\n")

    if (first == answer1):
        print("The answer is correct\n")
        count = count + 1
        secondquestion(count)

    else:
        secondquestion(count)
def secondquestion(count):

    print("You have made it to the second question, keep going!\n")

    first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if first == answer2:
        print("The answer is correct")
        count = count + 1
        thirthquestion(count)
    else:
        print("Hint:Bigger than 1 ")
        first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if (first == answer2):
        print("The answer is correct")
        count = count + 1
        thirthquestion(count)
    else:
        print("Hint:Smaller than 2")
        first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if (first == answer2):
        print("The answer is correct")
        count = count + 1
        thirthquestion(count)

    else:
        thirthquestion(count)
def thirthquestion(count):

    print(" keep going, you can do this!!\n")

    first = input("Which is the longest river in the world?\n")

    if first == answer3:
        print("The answer is correct\n")
        count = count + 1
        fourthquestion(count)
    else:
        print("Hint:It is considered the lung of the planet \n")
        first = input("Which is the longest river in the world?\n")

    if (first == answer3):
        print("The answer is correct\n")
        count = count + 1
        fourthquestion(count)
    else:
        print("Hint:It is in America")
        first = input("Which is the longest river in the world?\n")

    if (first == answer3):
        print("The answer is correct\n")
        count = count + 1
        fourthquestion(count)

    else:
        fourthquestion(count)
def fourthquestion(count):
    print("You are already half way,the questions are getting harder")

    first = input("What country joined England to form the United Kingdom in 1707?\n")

    if first == answer4:
        print("The answer is correct\n")
        count = count + 1
        fithquention(count)
    else:
        print("Hint:Lake ness is in it \n")
        first = input("What country joined England to form the United Kingdom in 1707?\n")

    if (first == answer4):
        print("The answer is correct\n")
        count = count + 1
        fithquention(count)
    else:
        print("Hint:Edinburgh is the capital city")
        first = input("What country joined England to form the United Kingdom in 1707?\n")
        finish(count)

    if (first == answer4):
        print("The answer is correct\n")
        count = count + 1
        fithquention(count)

    else:

        fithquention(count)
def fithquention(count):


        print("Last one,go hard!")

        first = input("What is the biggest planet on the milky way?\n")

        if first == answer5:
            print("The answer is correct\n")
            count = count + 1
            finish(count)

        else:
            print("It is 11,2 time bigger than the earth \n")
            first = input("What is the biggest planet on the milky way?\n")

        if (first == answer5):
            print("The answer is correct\n")
            count = count + 1
            finish(count)
        else:
            print("It is made by gas")
            first = input("What is the biggest planet on the milky way?\n")
            finish(count)

        if (first == answer5):
            print("The answer is correct\n")
            count = count + 1
            finish(count)

        else:

            finish(count)
def finish(count):
    print("Congratulations you have finished the game!!!")
    print("Your score is:", count)

menu()










