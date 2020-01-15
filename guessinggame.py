from random import randint

# This is a guessing game program. This is the starting point of the game.
def start_game():

    # Created a list that will store each guess
    your_guess = []

    # Created a function that will generate a random number
    random_number = computer_random_number()

    # prints or diplays a introduction message
    print("The computer is thinking of a numeber")

    # A while loop that will keep iterating after each guess. Once the guess is correct the while loop will break
    while True:
        # This guess function will ask the user the question
        guess = asking_the_guess_question();

        # This will take the users guess and append it to the list
        your_guess.append(guess)

        # This is a passing method that will take the guess and random_number
        results = checkTheNumber(random_number, guess)

        # Will check if results are False
        if results == False:
            # breaks the loop
            break

    # Prints into display
    print(f"You made {len(your_guess)} guesses")


# Function that will generate a random number from 1 - 100
def computer_random_number():
    return randint(1,100)


# Function to ask the user a question for each value
def asking_the_guess_question():
    return int(input("What number do you guess? :"))



# Function to compare the random number to the number that user has guessed
def checkTheNumber(random_number, guess):

    # if the number of the guess is greater than the random number
    if random_number < guess:
        print("Your to high")
        return True

        # if the number of the guess is lower than the random number
    elif random_number > guess:
        print("Your to low")
        return True

        # if the number of the guess is the exact pick 
    else:
        print("You picked the right number!")
        return False

if __name__ == '__main__':
    start_game()
