import connect4
import hangman
import quizFinal

c = 1

while c == 1:
    print("Welcome to our minigame selector!")
    print("Select one of the games to be played.")
    print("\t 1- Connect4")
    print("\t 2- Hangman")
    print("\t 3- Quiz")
    print("\t 4- Guess the word")
    print("\t 5- Exit")

    opt = int(input("\nSelect the option."))

    match opt:
        case 1:
            connect4.init()
            break
        case 2:
            name = hangman.name()
            hangman.hangmangame(name)
            break
        case 3:
            quizFinal.quiz()
            break



