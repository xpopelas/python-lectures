# In this exercise, we want to look into sequences and for loops.
# As was the case before, we will start with a skeleton of a code, where you can do a few things with sequences.


def get_fibonacci_sequence(length):
    """
    In this function, you want to return a list of the first length numbers of the Fibonacci sequence.

    The Fibonacci sequence is a sequence of numbers, where the next number is the sum of the previous two numbers.
    The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Since the sequence is infinite, we will only look at the first length numbers of the sequence.

    Create a function, that will take the parameter length, which is the length of the sequence that you want to return.
    Return list of the first length numbers of the Fibonacci sequence.

    >> get_fibonacci_sequence(0)
    []

    >> get_fibonacci_sequence(1)
    [0]

    >> get_fibonacci_sequence(5)
    [0, 1, 1, 2, 3]
    """
    ...


def calculate_factorial(max_number):
    """
    In this function, you want to return a dictionary of factorials of all numbers from 0 to max_number.

    The factorial of a number is the product of all positive integers less than or equal to the number.
    The factorial of 0 is 1.

    Create a function, that will take the parameter max_number, which is the maximum number of the sequence that you want to return.
    Return list of factorials of all numbers from 0 to max_number.

    >> calculate_factorial(0)
    {0: 1}

    >> calculate_factorial(1)
    {0: 1, 1: 1}

    >> calculate_factorial(5)
    {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    """
    ...


def is_palindrome(text):
    """
    In this function, you want to check if the given text is a palindrome.

    Palindrome is a text, that is the same when read backwards.

    If the given text is a palindrome, return True, otherwise return False.

    We want to make sure, that the function is case-insensitive, so "Anna" is a palindrome, and so is "anna".

    >> is_palindrome("Anna")
    True

    >> is_palindrome("anna")
    True

    >> is_palindrome("Hello")
    False

    >> is_palindrome("RaceCar")
    True
    """
    ...


def main():
    # This is the main function, where you can call the functions that you have defined above.
    # Feel free to add any code here that you want to test.
    ...


if __name__ == "__main__":
    main()