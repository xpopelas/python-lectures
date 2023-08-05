# This will be the first homework assignment. You will need to create a program, which can take a string and print it in a billboard-like style.
# The program should also be able to take a number and print it in a billboard-like style, too.

# In this case, the billboard will be very simple, it will only have a border around every single letter.
# Let's say we would want to create a billboard for the word "Python", it would look like this:
# ***** ***** ***** ***** ***** *****
# *   * *   * *   * *   * *   * *   *
# * P * * Y * * T * * H * * O * * N *
# *   * *   * *   * *   * *   * *   *
# ***** ***** ***** ***** ***** *****

# However, since the customer also wanted to have a billboard for numbers, and they wanted it to be readable, this will be printed differently.
# Let's say that customer would like a billboard for the number 1234, it would look like this:
# ***********
# *         *
# * 1 2 3 4 *
# *         *
# ***********

# As you can see, every letter is surrounded by a border of asterisks (*).
# Additionally, every letter is in upper case, so you will need to convert the string to upper case before printing it.

def print_billboard(message):
    # In this function, you have to print the message in a billboard-like style.
    # This function doesn't have to return anything. Additionally, if you feel like you need a different function for this task, you can create one.
    # PRO TIP: You can separate the functionality into a case for strings and a case for numbers.
    ...

def main():
    # In this function, try to ask a user for their input, and then print it in a billboard-like style.
    # If user gives you an empty string, tell them that they forgot the message and ask them again.
    ...

if __name__ == "__main__":
    main()
