# In this practice exercise, we will look into variables and mathematical operations.

# Below, I have prepared a short skeleton of a code, that will allow you to specify different shapes and calculate their area.
# The code is not complete, you will need to add some code to make it work - I have marked the places where you need to add code with TODO comments.


def area_of_square(side):
    area = ...  # TODO: Calculate the area of a square with the given side
    return area


def area_of_rectangle(width, height):
    area = ...  # TODO: Calculate the area of a rectangle with the given width and height
    return area

def area_of_circle(diameter):
    PI = 3.1415
    area = ...  # TODO: Calculate the area of a circle with the given diameter
    return area

def area_of_triangle(base, height):
    area = ...  # TODO: Calculate the area of a triangle with the given base and height
    return area


# This function is used to run the program. No changes are needed here.
# If you want to run the program, you need to click on the green arrow/triangle next to the if statement and select Run.
def main():
    shape = input("What shape do you want to calculate the area of? (square, rectangle, circle, triangle): ")
    while shape not in ["square", "rectangle", "circle", "triangle"]:
        print("Invalid shape!")
        shape = input("What shape do you want to calculate the area of? (square, rectangle, circle, triangle): ")
    if shape == "square":
        side = input("What is the side of the square? ")
        while not side.isdigit():
            print("Invalid side!")
            side = input("What is the side of the square? ")
        print(f"The area of the square is {area_of_square(int(side))}")
    elif shape == "rectangle":
        width = input("What is the width of the rectangle? ")
        while not width.isdigit():
            print("Invalid width!")
            width = input("What is the width of the rectangle? ")
        height = input("What is the height of the rectangle? ")
        while not height.isdigit():
            print("Invalid height!")
            height = input("What is the height of the rectangle? ")
        print(f"The area of the rectangle is {area_of_rectangle(int(width), int(height))}")
    elif shape == "circle":
        radius = input("What is the radius of the circle? ")
        while not radius.isdigit():
            print("Invalid radius!")
            radius = input("What is the radius of the circle? ")
        print(f"The area of the circle is {area_of_circle(int(radius))}")
    elif shape == "triangle":
        base = input("What is the base of the triangle? ")
        while not base.isdigit():
            print("Invalid base!")
            base = input("What is the base of the triangle? ")
        height = input("What is the height of the triangle? ")
        while not height.isdigit():
            print("Invalid height!")
            height = input("What is the height of the triangle? ")
        print(f"The area of the triangle is {area_of_triangle(int(base), int(height))}")


if __name__ == "__main__":
    main()
