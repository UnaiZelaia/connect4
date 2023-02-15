def quiz():
    import time
    ans = "yes"
    while ans == "yes":
        print("Welcome to our trivia quiz!")
        name = input("Whats your name? ")
        play = str(input("Well, " + name + " do you wanna play? "))
        if play == "yes":
            starttime = time.time()
            score = 0
            print("Question 1: What is the capital of France?")
            print("A. London")
            print("B. Paris")
            print("C. Madrid")
            print("D. Berlin")
            answer1 = input("Enter your answer (A, B, C, or D): ")
            if answer1 == "B":
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

            print("Question 2: What is the largest planet in our solar system?")
            print("A. Mars")
            print("B. Jupiter")
            print("C. Venus")
            print("D. Saturn")
            answer2 = input("Enter your answer (A, B, C, or D): ")
            if answer2 == "B":
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

            print("Question 3: What is the tallest mammal in the world?")
            print("A. Elephant")
            print("B. Giraffe")
            print("C. Lion")
            print("D. Hippopotamus")
            answer3 = input("Enter your answer (A, B, C, or D): ")
            if answer3 == "B":
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

            print("Question 4: How old is the earth?")
            print("A. 4.54 billion")
            print("B. 2023")
            print("C. 50480")
            print("D. 9000")
            answer4 = input("Enter your answer (A, B, C, or D): ")
            if answer4 == "A":
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

            print("Question 5: What is the largest ocean?")
            print("A. Indian")
            print("B. Atlantic")
            print("C. Artic")
            print("D. Pacific")
            answer5 = input("Enter your answer (A, B, C, or D): ")
            if answer5 == "D":
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
            totaltime = round((time.time() - starttime), 2)
            print("Your score is:", score, "/5")
            print("in only " + str(totaltime) + " seconds.")
        # Ask the user if they want to replay the program
        ans = str(input("Do you want to replay again the program? "))
        ans.lower()
        if ans == "no":
            exit()


quiz()
