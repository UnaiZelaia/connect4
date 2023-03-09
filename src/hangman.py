#imports
import time
import random

#animals = ["ferret", "cockatoo", "hedgehog", "raccoon", "vulture", "ostrich", "python", "peacock", "marmot",
              # "condor"]
animals = []

# Functions for hangman
def name():

    playername = input("What's your name? ")
    return 0

def hangmangame(playername):

    a = 1

    print(" ")
    for i in range(1, 4):
        print("Loading the game...")
        time.sleep(1)

    f = open("../files/hangman/animals.csv", "r")

    while a != 0:
        file_line = f.readline()
        animals.append(file_line.strip())

        if not file_line:
            a = 0
        else:
            a = a + 1

    wronganswer = []

    word = random.choice(animals)

    print(" ")
    print("Guess the characters")
    print(" ")

    guesses = ""

    # we put how many chances has the user
    turns = 15

    while turns > 0:

        # counts the number of times the user fails
        failed = 0

        # we look is the input is in the word
        for char in word:

            # comparing that character with the character in guesses
            if char in guesses:
                print(char, end=" ")

            else:
                print("_", end=" ")

                # every time the user fails it will count
                failed += 1

        print(" ")

        if failed == 0:
            print(" ")
            print(" ")
            print("Congratulations " + str(playername) + " :) you have win!!!")
            print(" ")

            print("The word is: ", word)
            print(" ")
            break

        # if he enters the wrong character, he will enter another
        print(" ")
        guess = input("Try a character: ")
        print(" ")

        # every input character will be stored in guesses
        guesses += guess

        # check input with the character in word
        if guess not in word:

            turns -= 1

            print("Wrong answer :( please try again")
            print(" ")

            if guess not in wronganswer:
                print("Failed characters")
                wronganswer.append(guess)
                print(wronganswer)
                print(" ")
            else:
                print("You have already try this character! Pay attention " + playername + "! This try is not for free!")
                print(" ")
                print("Failed characters")
                print(wronganswer)
                print(" ")

            print("You have", + turns, "more guesses")
            print(" ")

            if turns == 0:
                print(" ")
                print("You Loose :(")
                print(" ")


    print("Thanks for playing " + str(playername) + " hope to see you here again!!!")
    print(" ")
    f.close()


