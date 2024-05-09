# Python quiz

questions = [
    {
    'question': '1+1 ?',
    'options': [1, 2, 3, 'Skip', 'Exit'],
    'answer': 2
    },
    {
    'question': '5+1 ?',
    'options': [5, 6, 8, 'Skip', 'Exit'],
    'answer': 6
    },
    {
    'question': '10 - 5 ?',
    'options': [5, 10, 2, 'Skip', 'Exit'],
    'answer': 5
    },
    {
    'question': '1 * 5 ?',
    'options': [5, 10, 15, 'Skip', 'Exit'],
    'answer': 5
    }
]

right_anwser = 0

for j, question in enumerate(questions):
    print('Question ', j+1, ': ', question['question'])
    for i, option in enumerate(question['options']):
        print('Ans', i+1 ,': ', option)

    answer = int(input("Enter your anwser : "))
    
    #print(question['answer'])
    #print(question['options'][answer-1])
    #print(question['answer'])
 
    if(answer == 4):
        break
    elif(question['options'][answer-1] == question['answer']) :
        right_anwser +=1;
        print("Correct");   
    else :
        print(f"Wrong !, Correct answer is {question['answer']}")
        
    print(f"Your score is {right_anwser}/{len(questions)}")




# Second way

print("--------------Second solution ------------------")

quiz = {
    '1+1 ?': {
    'options': (1, 2, 3),
    'answer': 2
    },
    '5+1 ?': {
    'options': (5, 6, 8),
    'answer': 6
    },
    '10 - 5 ?': {
    'options': (5, 10, 2),
    'answer': 5
    },
    '1 * 5 ?': {
    'options': (5, 10, 15),
    'answer': 5
    }
}

i = 0;
score  = 0
for q in quiz:
    i = i+1
    print(f"Question {i}. {q}")
    _options = quiz[q]['options']
    print(f"Choose an option {_options}")
    _user_answer = int(input("Choose your answer:"))
    _answer = quiz[q]['answer']
    if(_user_answer == _answer) :
        score +=1;
        print("Your answer is correct")
    else:
        print("Wrong answer.")
        
    print(f"Your score is {score}/{len(quiz)}")
    
    
    
    

