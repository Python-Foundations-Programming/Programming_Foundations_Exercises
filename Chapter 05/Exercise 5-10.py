# Programming Exercise 5-10

import random

# main function
def main():
    # Local variables
    num1 = 0
    num2 = 0
    correctAnswer = 0
    userAnswer = 0

    # Get numbers
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    
    # Display math problem 
    displayProblem(num1,num2)

    # Get user answer
    userAnswer = getAnswer()

    # Calculate correct answer
    correctAnswer = num1 + num2

    # Display result
    showResult(correctAnswer, userAnswer)

# The displayProblem function accepts the numbers
# and displays them
def displayProblem(num1,num2):
    print (f'{num1:5}')
    print (f'+{num2:4}')
    
# The getAnswer function gets and returns the user answer
def getAnswer():
    inputAnswer = int(input('Enter sum of numbers: '))
    return inputAnswer
    
# The showResult function tells if user answer is
# correct or not
def showResult (correctAnswer, answer):
    if correctAnswer == answer:
        print ('Correct answer – Good Work!')
    else:
        print (f'Incorrect... The correct answer is: {correctAnswer}')

# Call the main function.
main()




