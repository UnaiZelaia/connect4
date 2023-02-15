def quiz():
    ans = "yes"
    while ans == "Yes":
        print("Question 1: What is the capital of France?")
        print("A. London")
        print("B. Paris")
        print("C. Madrid")
        print("D. Berlin")
        answer1 = input("Enter your answer (A, B, C, or D): ")

        print("Question 2: What is the largest planet in our solar system?")
        print("A. Mars")
        print("B. Jupiter")
        print("C. Venus")
        print("D. Saturn")
        answer2 = input("Enter your answer (A, B, C, or D): ")

        print("Question 3: What is the tallest mammal in the world?")
        print("A. Elephant")
        print("B. Giraffe")
        print("C. Lion")
        print("D. Hippopotamus")
        answer3 = input("Enter your answer (A, B, C, or D): ")

        print("Question 4: How old is the earth?")
        print("A. 4.54 billion")
        print("B. 2023")
        print("C. 50480")
        print("D. 9000")
        answer4 = input("Enter your answer (A, B, C, or D): ")

        print("Question 5: What is the largest ocean?")
        print("A. Indian")
        print("B. Atlantics")
        print("C. Artic")
        print("D. Pacific")
        answer5 = input("Enter your answer (A, B, C, or D): ")

        score = 0
        if answer1 == "B":
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            
        if answer2 == "B":
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            
        if answer3 == "B":
            print("Correct!")
            score += 1
        if answer4 == "A":
            print("Correct!")
            score += 1
        if answer5 == "D":
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            
        print("Your score is:", score, "/3")
    ans = input("Do you wanna play again?")
    if ans != "Yes" or "yes":
        exit()
