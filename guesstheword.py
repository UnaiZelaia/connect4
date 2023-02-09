import time;
loading=["Your game is loading...",3,2,1]
count=0

answer1="mercury"
answer2="1,6"
answer3="amazonas"
def menu():
  print("*================================*")
  print("Welcome to GuesstheWord game")

  for n in loading:
     print(n)
     time.sleep(0.7)


  firstquestion()


def firstquestion():

    first = input("What is the closest planet to the earth ?\n")

    if first == answer1:
        print("The answer is correct\n")
        ++count
        secondquestion()
    else:
        print("Hint:Old thermometers had it\n ")
        first = input("What is the closest planet to the sun?\n")

    if (first == answer1):
        print("The answer is correct\n")

        ++count
        secondquestion()
    else:
        print("Hint:Starts with the letter M\n")
        first = input("What is the closest planet to the sun?\n")

    if (first == answer1):
        print("The answer is correct\n")
        ++count
        secondquestion()

    else:
        secondquestion()




def secondquestion():

    print("You have made it to the second question, keep going!\n")

    first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if first == answer2:
        print("The answer is correct")
        ++count
        thirthquestion()
    else:
        print("Bigger than 1 ")
        first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if (first == answer2):
        print("The answer is correct")
        ++count
        thirthquestion()
    else:
        print("Smaller than 2")
        first = input("How many kilometres is a mile?(Write it with a coma)\n")

    if (first == answer2):
        print("The answer is correct")
        ++count
        thirthquestion()

    else:
        thirthquestion()





def thirthquestion():

    print(" keep going, you can do this!!\n")

    first = input("Which is the longest river in the world?\n")

    if first == answer3:
        print("The answer is correct\n")
        ++count
        fourthquestion()
    else:
        print("It is considered the lung of the planet \n")
        first = input("Which is the longest river in the world?\n")

    if (first == answer3):
        print("The answer is correct\n")
        ++count
        fourthquestion()
    else:
        print("It is in America")
        first = input("Which is the longest river in the world?\n")

    if (first == answer3):
        print("The answer is correct\n")
        ++count
        fourthquestion()

    else:
        fourthquestion()




def fourthquestion():
    print("You are already half way,the questions are getting harder")

    first = input("What country joined England to form the United Kingdom in 1707?\n")

    if first == answer3:
        print("The answer is correct\n")
        ++count
        finish()
    else:
        print("It is considered the lung of the planet \n")
        first = input("Which is the longest river in the world?\n")

    if (first == answer3):
        print("The answer is correct\n")
        ++count
        finish()
    else:
        print("It is in America")
        first = input("Which is the longest river in the world?\n")
        finish()

    if (first == answer3):
        print("The answer is correct\n")
        ++count
        finish()

    else:

        finish()






def finish():
    print(count)






menu()










