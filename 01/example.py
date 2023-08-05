# Hello there!
# In this small code, we will look into a small program, that gets the current date and time and prints it.
# Quick tip: Every line that starts with a # is a comment. Comments are used to explain what the code does and adds no functionality to the code.

import datetime
# ^ This is an import statement. It imports a module (in this case, the datetime module) so that we can use it in our code.
# You don't have to pay attention to this for now, we will cover it later.


# This is a function. Functions can be used to group code that does a specific task.
# This function returns the current date and time.
def get_current_date():
    return datetime.datetime.now()

# This is a variable. Variables are used to store essentially any data you want to have available.
# With this statement, we have created a variable called CURRENT_DATE and assigned it the value of the function get_current_date().
current_date = get_current_date()


# This is the main function. In our code, this function will be called first.
# This is not mandatory, but it is a good practice to have a main function.
# What this function does is that it gets the current date and time and prints it.
def main():
    print(f"Today's date is {current_date.day}-{current_date.month}-{current_date.year} and it's {current_date.hour}:{current_date.minute}:{current_date.second}")


# To run this code, we need to call the main function.
# Don't worry about the if statement for now, we will cover it later.
# To run the program, you should see a green arrow/triangle next to the if statement.
# Try clicking on it, select Run and see what happens :)
if __name__ == "__main__":
    main()