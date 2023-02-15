import connect4
import hangman
import quizFinal
import guesstheword
c = 1

while c == 1:
    print("Welcome to our minigame selector!")
    print("Select one of the games to be played.")
    print("\t 1- Connect4")
    print("\t 2- Hangman")
    print("\t 3- Quiz")
    print("\t 4- Guess the word")
    print("\t 5- Exit")

    opt = int(input("\nSelect the option: "))


    if opt == 1:
        connect4.init()
    elif opt == 2:
        name = hangman.name()
        hangman.hangmangame(name)
    elif opt == 3:
        quizFinal.quiz()
    elif opt == 4:
        guesstheword.menu()
    elif opt == 5:
        c = 0
    else:
        print("Select a correct value.")



