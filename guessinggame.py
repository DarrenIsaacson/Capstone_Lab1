from random import randint

# This is a guessing game program. This is the starting point of the game.
def start_game():

    # Created a list
    your_guess = []

    random_number = computer_random_number()
    print("The computer is thinking of a numeber")

    while True:
        guess = asking_the_guess_question();
        your_guess.append(guess)
        results = checkTheNumber(random_number, guess)

        if results == False:
            break


    print(f"You made {len(your_guess)} guesses")



def computer_random_number():
    return randint(1,100)



def asking_the_guess_question():
    return int(input("What number do you guess? :"))




def checkTheNumber(random_number, guess):
    if random_number < guess:
        print("Your to high")
        return True
    elif random_number > guess:
        print("Your to low")
        return True
    else:
        print("You picked the right number!")
        return False

if __name__ == '__main__':
    start_game()
