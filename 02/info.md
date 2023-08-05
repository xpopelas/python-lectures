# Variables, types, conditions, loops and functions

In this lecture, we are going to look into the basics of programming. 

We will learn about variables, data types, conditions, loops and functions.

## Variables

First of all, lets start with variables. Variables are essentially named "containers" for data. They can store data, and you can use them to access the data later on.

To create a variable, you can just write the name of the variable, and then assign a value to it. You can assign a value to a variable by using the `=` operator.

```python
one = 1  # Assigns value 1 to variable one
two = one + one  # We can even assign a value to a variable by using another variable

greeting = "Hello"  # We can also assign strings to variables

fibonacci_numbers = [1, 1, 2, 3, 5, 8, 13]  # We can also assign lists to variables
```

Variables are a much-needed thing in programming, because without them, you would have to write the same thing over and over again. For example, if you wanted to print the same thing multiple times, you would have to write it multiple times. With variables, you can just assign the value to a variable, and then use it down in your code.

In Python, you can basically assign anything to a variable. You can assign numbers, strings, lists, dictionaries, and much more. We will look into these data types later on.

What is different in Python in comparison to many other languages is that you don't have to specify the type of the variable. In many other languages, you have to specify the type of the variable when you create it. For example, in Java, you would have to write `int one = 1;` to create a variable called `one` with the value of `1`. In Python, you don't have to do that. You can just write `one = 1` and Python will automatically know that the variable is an integer.

## Data types

As I mentioned earlier, you can assign different data types to variables. In this lecture, we will look into the most common data types in Python.

### Integers

Integers are basically any whole numbers (positive or negative). You can assign integers to variables by just writing the number.

Since these values represent numbers, they have all the common operations that you might want to do, such as addition, subtraction, multiplication, and division.

```python
one = 1
two = one + 1  # We added one and 1 together, and assigned the result to variable two

seven = 7
three = seven - 4  # We subtracted 4 from seven, and assigned the result to variable three

four = two * 2  # We multiplied two and 2 together, and assigned the result to variable four

five = 10 / 2  # We divided 10 by 2, and assigned the result to variable five
six = 12 // 2  # You can also do division with two slashes. This is called floor division, and it rounds the result down to the nearest integer.
```

### Floats

Float numbers represent decimal numbers. You can assign float numbers to variables by just writing the number with a decimal point. Don't use decimal commas, because Python doesn't understand them.

Float numbers also have all the common operations that you might want to do, such as addition, subtraction, multiplication, and division.

```python
one = 1.0  # This is theoretically a float number, but since it doesn't have any decimal places, Python will treat it as an integer

almost_pi = 3.1415  # This is a float number with decimal places

five = 2.5 * 2  # While we have used a float number on the left, and an integer on the right, the result will still be a float number. This result represents 5.0, which is a theoretically a float number. 

three_quarters = 3 / 4  # This is a float number, because the result of the division is a float number
zero = 3 // 4  # But in this case, you would get an integer, because the result of the "floor division" is an integer
```

### Strings

Strings represent any text. You can assign strings to variables by writing the text inside quotation marks.

Strings also have some operations that you can do with them. For example, you can add strings together, and you can also multiply strings with integers.

```python
hello = "Hello"  # This is a string
world = 'World'  # This is also a string - notice that we didn't use "double quotes" here, but 'single quotes' instead. Both of these are valid ways to create strings.

hello_world = hello + " " + world  # We added the strings together, and assigned the result to variable hello_world. Notice that we also added a space between the two strings.
print(hello_world)  # This will print "Hello World"

hello_world = hello * 3  # Funnily enough, you can also multiply strings by integers. This variable is now "HelloHelloHello"

# You can also "convert" different types to strings by using the str() function
number = 1
number_as_string = str(number)  # This will convert the number to a string, and assign it to variable number_as_string

# You can also convert strings to integers by using the int() function
number_as_string = "1"
number = int(number_as_string)  # This will convert the string to an integer, and assign it to variable number

# You can also convert strings to floats by using the float() function
number_as_string = "1.3"
number = float(number_as_string)  # This will convert the string to a float, and assign it to variable number

# And you can even find the length of the string by using the len() function
length = len("Hello")  # This will assign the length of the string "Hello" to variable length - in this case, the length is 5

# There is a lot of string functions and methods (such as one for turning everything into upper or lower case, to reverse them or check if they are a number, etc.), but it would take a lot of time to list them all.
# If you can imagine it, it exists! Best way to discover these functions on your own is to ask Google, for example questions like "How to reverse a string in Python" or "How to check if a string is a number in Python".
```

### Booleans

Booleans are the "truth values" of Python. They can either be `True` or `False`. You can assign booleans to variables by just writing `True` or `False`.

There are also operators that return booleans. For example, you can check if two values are equal to each other by using the `==` operator. This operator will return `True` if the values are equal, and `False` if they are not.

```python
this_is_true = True  # This is a boolean with the value of True
this_is_false = False  # This is a boolean with the value of False

this_should_be_true = 1 == 1  # In this case, we used an equality operator to check if 1 is equal to 1. Since it is, the result is True
this_should_be_false = 1 == 2  # In this case, we used an equality operator to check if 1 is equal to 2. Since it is not, the result is False

this_should_be_true_too = 1 != 2  # In this case, we used an inequality operator to check if 1 is not equal to 2. Since it is not, the result is True
this_should_be_false_too = 1 != 1  # In this case, we used an inequality operator to check if 1 is not equal to 1. Since it is, the result is False
```

In the code above, we have also hinted at the fact that there are also operators that return booleans. These operators are called "comparison operators", and they are used to compare two values. The most common comparison operators are:
- `==` - Checks if two values are equal to each other
- `!=` - Checks if two values are not equal to each other
- `>` - Checks if the value on the left is greater than the value on the right
- `<` - Checks if the value on the left is less than the value on the right
- `>=` - Checks if the value on the left is greater than or equal to the value on the right
- `<=` - Checks if the value on the left is less than or equal to the value on the right
- `is` - Checks if two values are the same object - this might seem like it's the same as the `==` operator, but it's not. We will look into this later on.
- `not` - Negates a boolean value - this is not really a comparison operator, but it's still a boolean operator
- `and` - Checks if both of the values are `True` - example: `True and True` will return `True`, but `True and False` will return `False`
- `or` - Checks if at least one of the values is `True` - example: `True or False` will return `True`, but `False or False` will return `False`
- `in` - Checks if the value on the left is in the value on the right - example: `1 in [1, 2, 3]` will return `True`, but `4 in [1, 2, 3]` will return `False`

### None

None is a special value in Python. It represents "nothing". You can assign None to variables by just writing `None`.

It might seem like it's weird to have a value that represents "nothing", but it's actually very useful.

For example, if you have a function that returns a value, but you don't want to return anything, you can just return None.


### Tuples

Tuples are a collection of values. You can assign tuples to variables by writing the values inside parentheses, and separating them with commas.

Tuples also have some operations that you can do with them. For example, you can add tuples together, and you can also multiply tuples with integers.

```python
my_tuple = ()  # This creates an empty tuple

# You can also create a tuple with values inside it
my_tuple = (1, 2, 3)  # This is a tuple with 3 values inside it

# You can also create a tuple with just one value inside it
my_tuple = (1,)  # This is a tuple with just one value inside it. Notice the comma after the value - this is important, because otherwise Python will think that you just wrote a number inside parentheses, and not a tuple

# You can also create a tuple without parentheses
my_tuple = 1, 2, 3  # This is a tuple with 3 values inside it
```

### Lists

Lists are a collection of values. While lists might seem similar to tuples at first, the key difference is that lists are able to change their size, and you can add values inside of it. 

You can assign lists to variables by writing the values inside square brackets, and separating them with commas.

Lists also have some operations that you can do with them. For example, you can add lists together, and you can also multiply lists with integers.

```python
my_list = []  # This creates an empty list
my_list = [1, 2, 3]  # You can also create a list with values inside it
my_list = [1, "Hello", True]  # You can also have different types of values inside a list

# To access any specific value inside a list, you can use the index operator. 
# The index operator is just a pair of square brackets, and you put the index of the value you want to access inside them.
# However, beware: while most normal people count from 1, programmers count from 0. 
# This means that the first value in a list is at index 0, the second value is at index 1, and so on.

hello = my_list[1]  # This will assign the value "Hello" to the variable hello
print([0, 1, 2, 3, 4, 5][3])  # This will print 3, because the value at index 3 is 3

# Now, let's say that I want to add some value to the list. I can do that by using the append method.
# Whenever something is a "method", it means it has to be called directly on the variable itself.
# In this case, we are calling the append method on the my_list variable.
my_list.append(4)  # This will add the value 4 to the end of the list

# You can also find the length of the list by using the len function
print(len(my_list))  # This will print 4, because the length of the list is 4

# There are also a looot of different ways to interact with lists. For now, let's leave it as is, and we will get back to it later on.
```

### Sets

Sets are a collection of values. You can assign sets to variables by writing the values inside curly brackets, and separating them with commas.

Sets might seem like a list, but they are actually very different. The main difference is that sets can't have duplicate values.

Additionally, sets are unordered, which means that you can't access the values inside them by using an index.

And lastly, you can't have "mutable" values inside a set.

While we haven't looked into what "mutable" means, this means that you can't variables/values that can be changed.

This means that you can't have lists inside a set, but you can have tuples.

```python
my_set = set()  # This creates an empty set
my_set = {1, 2, 3}  # You can also create a set with values inside it

# You can also add values to the set by using the add method
my_set.add(4)  # This will add the value 4 to the set

# Sets are useful to check, if a value is inside a set
# For this, we use the boolean operator "in", which we mentioned above.
# This operator checks if the value on the left is in the value on the right.
print(1 in {1, 2, 3})  # This will print True, because 1 is in the set
print(4 in {1, 2, 3})  # This will print False, because 4 is not in the set
```

### Dictionaries

Dictionaries are once again a collection of values, however they are a bit different. You can think of them as traditional dictionaries, where you have one word, and then you have the definition of that word.

In Python, dictionaries are a collection of key-value pairs. You can assign dictionaries to variables by writing the key-value pairs inside curly brackets, and separating them with commas. You also have to separate the key and the value with a colon.

Keys don't necessarily have to be just strings, they can be any value, but they have to be "immutable" (therefore not changeable).

```python
my_dict = {}  # This creates an empty dictionary
my_dict = {"Hello": "Used as a greeting or to begin a phone conversation", "World": "the earth, together with all of its countries and peoples"}  # You can also create a dictionary with key-value pairs inside it

# You can also add key-value pairs to the dictionary by using the index operator
my_dict["Python"] = "A large heavy-bodied nonvenomous constrictor snake occurring throughout the Old World tropics"

# And you can access the values by specifying a key in the index operator
print(my_dict["Hello"])  # This will print "Used as a greeting or to begin a phone conversation"

# You can also check if a key is in the dictionary by using the "in" operator
print("Hello" in my_dict)  # This will print True, because "Hello" is a key in the dictionary
print("Goodbye" in my_dict)  # This will print False, because "Goodbye" is not a key in the dictionary
```

## Conditions

Now that we have established the basic data types, let's look at how we can use them to make decisions.

Often in programming, you want to have a specific piece of code run only if a certain condition is met.

For example, let's say that you want to print "Hello" only if the variable `name` is equal to "John".

You can do this by using the `if` statement.

```python
name = "John"

if name == "John":
    print("Hello")  # This will print "Hello", because the variable name is equal to "John"

name = "Peter"

if name == "John":
    print("Hello")  # This will not print anything, because the variable name is not equal to "John"
```

You can also use the `else` statement to specify what should happen if the condition is not met.

```python
name = "John"

if name == "John":
    print("Hello")  # This will print "Hello", because the variable name is equal to "John"
else:
    print("Goodbye")  # This will not print anything, because the variable name is equal to "John"

name = "Peter"

if name == "John":
    print("Hello")  # This will not print anything, because the variable name is not equal to "John"
else:
    print("Goodbye")  # This will print "Goodbye", because the variable name is not equal to "John"
```

Additionally, you might also want to do multiple checks. For this, you can use the `elif` statement - this literally translates to "else if".

```python
name = "John"

if name == "John":
    print("Hello John")  # This will print "Hello", because the variable name is equal to "John"
elif name == "Peter":
    print("Goodbye Peter")  # This will not happen in our case
else:
    print("Name not recognized")  # This will not happen in our case

name = "Peter"

if name == "John":
    print("Hello John")  # This will not happen in our case
elif name == "Peter":
    print("Goodbye Peter")  # This will print "Goodbye Peter", because the variable name is equal to "Peter"
else:
    print("Name not recognized")  # This will not happen in our case

name = "Jane"

if name == "John":
    print("Hello John")  # This will not happen in our case
elif name == "Peter":
    print("Goodbye Peter")  # This will not happen in our case
else:
    print("Name not recognized")  # This will print "Name not recognized", because the variable name is not equal to "John" or "Peter"
```

If statements can become really useful in cases, where you have an application, which depends on user input.

## Loops

Loops are a way to repeat a piece of code multiple times. There are two main types of loops in Python - `for` loops and `while` loops.

### For loops

For loops are used to repeat a piece of code for a specific number of times. You can use them to iterate over a list, a tuple, a set, a dictionary or a string.

```python
# Let's say that we want to greet multiple of our friends
my_friends = ["John", "Peter", "Adam"]

# Now to iterate over the list, we can use the for loop
# To specify the loop, we have to specify for which of the values in the list we want to loop
for friend in my_friends:
    print("Hello " + friend)  # This will print "Hello John", "Hello Peter" and "Hello Adam"

# Notice the use the in operator, which we have used before to check if a value is in a set. In this case, we use it to specify the list, over which we want to iterate.

# We can also use the for loop to iterate over a string
my_string = "Hello"

for character in my_string:
    print(character)  # This will print "H", "e", "l", "l", "o"

# We can also use the for loop to iterate over a `range` of numbers. To do so, we use the `range` function.
# The range can use multiple amount of parameters. 
# When calling it with one parameter, it will create a range from 0 to the specified number.
for number in range(5):
    print(number)  # This will print 0, 1, 2, 3, 4

# When calling it with two parameters, it will create a range from the first parameter to the second parameter.
for number in range(2, 5):
    print(number)  # This will print 2, 3, 4
# Notice that the number 5 is not included in the range

# When calling it with three parameters, it will create a range from the first parameter to the second parameter, with the step size of the third parameter.
for number in range(2, 10, 2):
    print(number)  # This will print 2, 4, 6, 8
```

### While loops

While loops are used to repeat a piece of code **while** a certain condition is met.

```python
# Let's say that we want to count from 0 to 4
# When working with for loops, we have to specify the range of numbers, which we want to iterate over
for number in range(5):
    print(number)  # This will print 0, 1, 2, 3, 4

# You can achieve the same result with a while loop
# To specify the loop, we have to specify the condition, which has to be met for the loop to continue

number = 0
while number < 5:
    print(number)  # This will print 0, 1, 2, 3, 4
    number = number + 1
```

## Functions

The last thing we will look at in this session are functions. Functions are a way to group a piece of code together, so that you can reuse it multiple times.

```python
# In this case, let's say that we want to greet a person, and at the same time tell them what is their favorite color
# We will store the name of our friends in a list, and their favorite color in the dictionary

my_friends = ["John", "Peter", "Adam"]
my_friends_favorite_colors = {
    "John": "red",
    "Peter": "green",
    "Adam": "pearlescent blue",
}

# Now we could do this the traditional way, and write the code for each of our friends separately:
print("Hello " + my_friends[0] + ", your favorite color is " + my_friends_favorite_colors[my_friends[0]])
print("Hello " + my_friends[1] + ", your favorite color is " + my_friends_favorite_colors[my_friends[1]])
print("Hello " + my_friends[2] + ", your favorite color is " + my_friends_favorite_colors[my_friends[2]])

# But this is not very efficient, and it is also not very readable
# You might also consider doing this with a for loop, which would certainly be better.
for friend in my_friends:
    print("Hello " + friend + ", your favorite color is " + my_friends_favorite_colors[friend])

# But what if we wanted to do this multiple times in our code?
# We could copy the for loop, but that would be very inefficient, and it would also be very hard to maintain.
# Let's say that we would want to change this some time later on, so that we do not include the color in the greeting.
# We would have to change it in multiple places, which can be annoying.

# This is where functions come in handy
# We can define a function, which will do the greeting for us
# To define a function, we use the `def` keyword, followed by the name of the function, and the parameters, which the function takes
# In our case, we will have one parameter, which will be the name of the friend
def greet_friend(friend):
    print("Hello " + friend + ", your favorite color is " + my_friends_favorite_colors[friend])

# Now we can call the function for each of our friends
for friend in my_friends:
    greet_friend(friend)

# This greatly improves the readability of our code, and it also makes it easier to maintain.

# We can also define functions, which do not take any parameters
def greet_schembulak():
    print("Hello Schembulak!")
```

Functions can also be used to calculate the value of something, and return it.

```python
# Let's say that we want to calculate the area of a rectangle
# We will define a function, which will take the width and the height of the rectangle as parameters, and return the area of the rectangle
def calculate_area_of_rectangle(width, height):
    return width * height  # This will return the value of the width multiplied by the height

# Now we can call the function, and store the result in a variable
area_of_rectangle = calculate_area_of_rectangle(5, 10)
```
