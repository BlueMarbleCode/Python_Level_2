# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program - Review
# Comprehensive Review of Key Python Concepts
#
# NOTE: This file reviews the main Python concepts you've learned so far.
#       Go through each section and try to complete the exercises!

# ==============================================================================
# 1. Variables and Data Types

# Variables store values that you can use later in your program.
name = "Alice"  # String
age = 12        # Integer
height = 1.6    # Float
is_student = True  # Boolean

# Let's print the values stored in the variables
print(f"Name: {name}, Age: {age}, Height: {height}, Is a student: {is_student}")

# Practice:
# Create variables to store your favorite color, number, and a fact about you.


# ==============================================================================
# 2. Basic Arithmetic

# You can use Python for basic math operations:
a = 10
b = 5

addition = a + b  # Adds a and b
subtraction = a - b  # Subtracts b from a
multiplication = a * b  # Multiplies a by b
division = a / b  # Divides a by b

# Print the results
print(f"Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}, Exponent: {exponent}")

# Practice:
# Create two numbers and calculate the sum, difference, product, and quotient.


# ==============================================================================
# 3. Conditionals (if, elif, else)

# Conditional statements let you check if something is true, and then do something based on that.
if age > 10:
    print(f"{name} is older than 10!")
elif age == 10:
    print(f"{name} is exactly 10!")
else:
    print(f"{name} is younger than 10!")

# Practice:
# Write a conditional that checks if your favorite number is greater than 50, less than 50, or exactly 50.


# ==============================================================================
# 4. Loops (for, while)

# A for loop lets you repeat a block of code for each item in a list or a range of numbers.
for i in range(5):  # Loop from 0 to 4
    print(f"Looping {i + 1} times")

# A while loop continues running as long as the condition is true.
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1  # Increase count by 1

# Practice:
# Write a for loop that prints the numbers from 1 to 10.
# Write a while loop that prints the numbers from 10 down to 1.


# ==============================================================================
# 5. Functions

# Functions let you group code into reusable pieces.
def greet_person(name):
    print(f"Hello, {name}!")

# Call the function
greet_person("Charlie")

# Functions can also return a result
def square_number(x):
    return x * x

result = square_number(4)
print(f"The square of 4 is {result}")

# Practice:
# Write a function that takes two numbers and returns their sum.
# Write a function that takes a number and returns whether it is even or odd.

# ==============================================================================
# 6. Lists

# A list is a collection of items stored in a single variable.
fruits = ["apple", "banana", "cherry"]

# Access items by their index (position)
print(f"My favorite fruit is {fruits[1]}")  # This prints "banana"

# Add items to the list
fruits.append("orange")
print(f"Updated fruits list: {fruits}")

# Loop through the list
for fruit in fruits:
    print(f"I like {fruit}")

# Practice:
# Create a list of your favorite foods and print each one.
# Add a new food to your list and print the updated list.

# ==============================================================================
# 7. Dictionaries

# A dictionary is a collection of key-value pairs.
student_info = {
    "name": "Alice",
    "age": 12,
    "grade": "7th"
}

# Access values by their key
print(f"Student's name: {student_info['name']}")

# Add a new key-value pair
student_info["favorite_subject"] = "Math"
print(f"Updated student info: {student_info}")

# Loop through the dictionary
for key, value in student_info.items():
    print(f"{key}: {value}")

# Practice:
# Create a dictionary to store information about your favorite movie (title, year, genre).
# Add a new key-value pair to the dictionary and print the updated dictionary.


# ==============================================================================
# 8. Input from Users

# You can get input from the user using the input() function.
user_name = input("What's your name? ")
print(f"Hello, {user_name}!")

# You can also ask the user for numbers, but remember to convert them to integers or floats.
user_age = int(input("How old are you? "))
print(f"You are {user_age} years old.")

# Practice:
# Ask the user for their favorite color and print a message including their color.
# Ask the user for two numbers and print their sum.


# ==============================================================================
# 9. Importing Libraries

# Python has many built-in libraries. You can import them to use special functions.
import random

# The random library can generate random numbers
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Practice:
# Use the random library to generate a random number between 1 and 100.
# Use a loop to let the user guess the random number.

# ==============================================================================
# 12. Review Practice Challenges

# Now it's time to combine what you've learned in some challenges!

# Write a program that generates a random number between 1 and 50. Let the user guess the number and tell them if their guess is too high, too low, or correct.
# Write a function that takes a list of numbers and returns the largest number.

