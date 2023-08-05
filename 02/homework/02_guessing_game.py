import random  # Ignore this, we will cover this in one of the next lessons.

# In this homework, you will create a guessing game.
# This game is just a basic "guess what number I am thinking of" game.


# The program will work as follows:
# 1. The computer will think of a number between 1 and 100 (inclusive).
# 2. The user will be asked to guess the number.
# 3. If the user's guess is incorrect, the user will be asked to guess again. The computer also tells the user if the number is higher or lower than the user's guess.
# 4. The game continues until the user guesses correctly.
# 5. When the user guesses correctly, the user will be congratulated and the program will tell him how many guesses it took them to guess correctly.
# 6. The program will then ask the user if they want to play again.
# 7. If the user wants to play again, the program will start over from step 1.

# Once you're done, you can try to make the game more interesting by adding some features:
# 1. Add a limit to the number of guesses the user can make. After certain number of guesses, the user will be told that they lost and the program will ask them if they want to play again.
# The program will tell them also about how what was the number they were trying to guess.
# 2. Let the user choose the range of numbers they want to guess from. If the range is incorrect (e.g. the user wants to guess from 100 to 1), tell them that the range is incorrect and ask them again.
# 3. Tell the user if their guess is "hot" or "cold". If the user's guess is within 10 numbers from the number the computer is thinking of, tell the user that their guess is "hot".


def generate_random_number(from_number, to_number):
    # Since we didn't yet cover packages and modules, I have prepared this function for you.
    # This function will generate a random number between from_number and to_number (inclusive).
    # You can use this function to generate a random number for the user to guess.
    return random.randint(from_number, to_number)


def main():
    # In this function, you should implement the "guessing game" functionality.
    # PRO TIP: Try to separate the functionality into functions, that do one specific thing.
    # PRO TIP: You can use the function generate_random_number(from_number, to_number) to generate a random number for the user to guess.
    ...


if __name__ == "__main__":
    main()
