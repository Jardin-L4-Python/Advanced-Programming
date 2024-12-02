#Exercise1: MathsQuiz

#This is a message to greet the user.
print("Welcome to the Arithmetic Math Quiz!")

#The print("") is to put spacing.
print("")

#This function will ask for the user's name.
def get_user_name():
    name = input("First! What is your name? ")
    print("")
    print(f"Hi {name}! Good luck in playing the game! Enjoy! :)")
    return name

name = get_user_name()

print("")

import random

#This is a short menu of difficulty level options for users to select.

#This function displays the difficulty menu.
def displayMenu():
    #Ask the user to select a difficulty level.
    print("TO START, SELECT A DIFFICULTY LEVEL")
    print("")
    print("1. Easy (Single-digit numbers)")
    print("2. Moderate (Double-digit numbers)")
    print("3. Advanced (Four-digit numbers)")
    print("")

    #Ask the user to enter the number of their selected level.
    choice = input("Enter the number of your selected level: ")

    #Show confirmation of the response to the user.
    if choice == "1":
        print("You have selected Easy: Single-digit numbers.")
        return 'Easy'
    elif choice == "2":
        print("You have selected Moderate: Double-digit numbers.")
        return 'Moderate'
    elif choice == "3":
        print("You have selected Advanced: Four-digit numbers.")
        return 'Advanced'
    else:
        print("Invalid selection. Please select a number between 1 and 3.")
        return None

#This function determines the values used in each question.
def randomInt(difficulty):
    if difficulty == 'Easy':
        return random.randint(1, 9)
    elif difficulty == 'Moderate':
        return random.randint(10, 99)
    elif difficulty == 'Advanced':
        return random.randint(1000, 9999)
    else:
        return 0

#This function randomly decides if the problem is addition or subtraction.
def decideOperation():
    return random.choice(["+", "-"])
    
#This function displays the question to the user.
def displayProblem(difficulty):
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()

    #Calculate the correct answer according on the process.
    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    #Display the problem to the user.
    print(f"What is {num1} {operation} {num2}?")
    return correct_answer

#This function is to check if the user's answer is incorrect or correct.
def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

#This function displays the results at the end after the user finishes the quiz.
def displayResults(score):
    print(f"Your total score is: {score}")
    if score == 100:
        print("Perfect! You scored 100/100!")
    elif score >= 80:
        print(f"Wow! You scored {score}/100!")
    elif score >= 50:
        print(f"Nice! You scored {score}/100!")
    elif score >= 30:
        print(f"Good effort! You scored {score}/100!")
    else:
        print(f"It's alright! Better luck next time! You scored {score}/100.")

#This function is to generate a random number based on the difficulty
def get_valid_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt)
        if valid_choices:
            if user_input.lower() in valid_choices:
                return user_input.lower()
            else:
                print(f"Invalid input. Please select from {', '.join(valid_choices)}.")
        else:
            try:
                return int(user_input)
            except ValueError:
                print("Please eter a valid number.")

#This is a main function that runs the whole quiz.
def runQuiz():
    while True:
        difficulty = displayMenu()
        if difficulty is None:
            continue

        score = 0

        #This will loop for 10 questions.
        for i in range(10):
            print(f"\nQUESTION {i + 1}:")
            correct_answer = displayProblem(difficulty)

            user_answer = get_valid_input("Your answer: ")

            if isCorrect(user_answer, correct_answer):
                print("Correct! You've earned 10 points!")
                score += 10
            else:
                print("Incorrect! Try again.")
                user_answer = get_valid_input("Your answer: ")

                if isCorrect(user_answer, correct_answer):
                    print("Correct! You've earned 5 points!")
                    score += 5
                else:
                    print(f"Incorrect again. The correct answer was {correct_answer}.")

        #This function displays the results at the end of the quiz.
        print("")
        displayResults(score)

        #This will ask the user if they want to play again.
        play_again = get_valid_input("\nNice play! Would you like to play again? (yes/no): ", ['yes', 'no'])
        if play_again == 'no':
            print("")
            print("Thank you for playing the Arithmetic Math Quiz! Bye bye! :)")
            #This will exit the loop and end the game.
            break
        
runQuiz()

