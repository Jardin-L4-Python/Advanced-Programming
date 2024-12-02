#Exercise2: Alexa tell me a Joke

import random

#This is a message to greet the user.
print("Welcome to 'Alexa tell me a Joke'! :)")

#The print("") is to put spacing.
print("")

#This function loads jokes from the file and return them as a list.
def load_jokes(filename):
    with open(filename, 'r') as file:
        jokes = file.readlines()

    cleaned_jokes = [joke.strip() for joke in jokes]

    joke_pairs = []
    for joke in cleaned_jokes:
        if '?' in joke:
            setup, punchline = joke.split('?', 1)
            setup = setup.strip() + '?'
            punchline = punchline.strip()
            joke_pairs.append((setup, punchline))
        else:
            joke_pairs.append((joke, "No punchline found"))

    return joke_pairs

#This function displays a random joke from the list of jokes.
def tell_jokes(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke
    print(setup)

    input("Press ENTER to show the punchline!")
    print(punchline)
    print("")

#This is the main function that controls the flow of the program.
def main():
    jokes = load_jokes('randomJokes.txt')

    while True:
        user_input = input('Type "Alexa tell me a joke" to hear a joke, or "quit" to exit: ').strip().lower()
        print("")

        if user_input == "alexa tell me a joke":
            tell_jokes(jokes)
        elif user_input == "quit":
            print("Bye bye! I hope the jokes gave you plenty of laughs! :)")
            break
        else:
            print("Oops! Invalid statement. Please type 'Alexa tell me a joke' or 'quit'.")

if __name__ == "__main__":
    main()



