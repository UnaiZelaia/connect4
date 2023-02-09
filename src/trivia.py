def quiz():
name = input('Whats your name? ')
ans = 'yes'
score = 0
print('Lets start the game ' + name + '!')
quiz = {
    1 : {
        'question' : 'What is the firs name of Iron Man?',
        'answer' : 'Tony'
    },
    2 : {
        'question' : 'How old is the earth?',
        'answer' : 'a'
    },
    3 : {
        'question' : 'Who was the first person that discover America?',
        'answer' : 'b'
    }
}
for question in quiz:
    attempts = 3
    while attempts > 0:
        print(quiz[question]['question'])
        answer = input('Enter the answer: ')
        check = check_ans(question, answer, attempts, score)
        if check:
            score +=1
            break
        attempts -= 1


while ans == 'yes':
    print(question)
