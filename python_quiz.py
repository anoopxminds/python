# Python quiz

questions = [
    {
    'question': '1+1 ?',
    'options': [1, 2, 3, 'Skip', 'Exit'],
    'answer': 1
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
        print("Wrong !, Correct answer is ", question['answer'])
        
    print("Your score is ", right_anwser , " out of ", len(questions))

