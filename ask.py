'''
def ask():

    userGrade = 0
    questionsList = ['a','b','c','d','e','f','g','h','i','j','k']
    
    #print question randomly 
    #user input
    #check if the input is valid
    #check if the input is "Y" or "N"
    #add score to userGrade

    #print the next question randomly
    #....

    #print the last question
    #...

    print('You got', userGrade, 'scores!')

ask()

'''

import random
def ask():
    user_score = 0

    # I would suggest making the question list a dictionary containing 
    # the questions and the answers:
    question_list = {'q1':'M', 'q2':'T', 'q3':'T'} #etc.

    # Get a shuffled list of the questions so that we can iterate through them:
    question_list_shuffled = random.sample(question_list.keys(), len(question_list)) 

    for question in question_list_shuffled: # loop through the questions and their answers.
        print(question)

        inputted_answer = input().strip().lower() 
        # strip makes sure the program ignores
        # leading and trailing whitespace, and lower makes
        # sure the program ignores lower and upper. 

        while inputted_answer not in ['m', 't']:
            # Keeping asking the user until they input 'M' or 'T'
            inputted_answer = input("Sorry, not a valid answer. Try again:\n").strip().lower()

        if inputted_answer == question_list[question].lower():
        # Compares the input to the key (answer) of the question in the dictionary.
            user_score += 10
        
    print(f'You got {user_score} scores!')
        
ask()