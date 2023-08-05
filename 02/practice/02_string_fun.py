# In this exercise, we will look into strings and for loops.

# Below, I have prepared a short skeleton of a code, where you can do a few things with strings.

# The code is not complete, you will need to add some code to make it work - I have marked the places where you need to add code with TODO comments.

def print_start_triangle(height):
    """
    In this function, you want to print a triangle of asterisks (*) with the given height.
    For example, if the height is 3, you want to print:
    *
    **
    ***
    Of course, we want to make it variable, so if the height is 5, you want to print:
    *
    **
    ***
    ****
    *****
    TODO: Print a triangle of asterisks (*) with the given height
    """
    print("*")


def print_end_triangle(height):
    """
    In this function, you want to print a triangle of asterisks (*) with the given height.
    For example, if the height is 3, you want to print:
    ***
    **
    *
    Of course, we want to make it variable, so if the height is 5, you want to print:
    *****
    ****
    ***
    **
    *
    TODO: Print a triangle of asterisks (*) with the given height
    """
    print("*")


def print_square(height):
    """
    In this function, you want to print a square of asterisks (*) with the given height.
    But now, the square inside has to be hollow (with spaces).
    For example, if the height is 3, you want to print:
    ***
    * *
    ***
    Of course, we want to make it variable, so if the height is 5, you want to print:
    *****
    *   *
    *   *
    *   *
    *****
    TODO: Print a square of asterisks (*) with the given height
    """
    print("*")


def print_diamond(height):
    """
    In this function, you want to print a diamond of asterisks (*) with the given height.
    For example, if the height is 3, you want to print:
      *
     ***
    *****
     ***
      *
    Of course, we want to make it variable, so if the height is 5, you want to print:
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    TODO: Print a diamond of asterisks (*) with the given height
    """
    print("*")


# Everything below is a program that will run the functions you have implemented, so you can see if everything is correct.


def main():
    print("Welcome to the string fun program!")
    print("Let's print some shapes!")
    print("Firstly we are going to start with triangles.")

    print_start_triangle(3)
    print_start_triangle(5)
    print_start_triangle(10)

    print("Now we are going to print triangles that end with asterisks.")

    print_end_triangle(3)
    print_end_triangle(5)
    print_end_triangle(10)

    print("Now lets make a wave of the triangles!")
    print_start_triangle(3)
    print_end_triangle(2)
    print_start_triangle(5)
    print_end_triangle(4)
    print_start_triangle(10)
    print_end_triangle(9)

    print("Now we are going to print squares.")
    print_square(3)
    print_square(5)
    print_square(10)

    print("And lastly, the diamonds.")
    print_diamond(3)
    print_diamond(5)
    print_diamond(10)


if __name__ == "__main__":
    main()
    