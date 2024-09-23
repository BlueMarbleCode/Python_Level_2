# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Big Nested Loop Example

# NOTE: Nested loops are loops inside other loops. They allow us to repeat
#       a set of actions multiple times within another repeated action!

# ==============================================================================
# Example: A number guessing game inside a loop
# The outer loop asks the user if they want to play the game again.
# The inner loop keeps asking them to guess a number until they get it right!

play_again = "yes"

while play_again == "yes": 
    secret_number = 3  
    guess = None  

    while guess != secret_number:  
        guess = int(input("Guess the secret number (between 1 and 5): "))
        if guess == secret_number:
            print("You got it! Great job!")
        else:
            print("Try again!")
    
    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")

# Stars Pyramid
# Write a nested for loop that prints the following pyramid of stars:
# 
# *
# **
# ***
# ****
# *****
# 
# Hint: The outer loop controls the number of rows, and the inner loop
# controls how many stars (*) appear in each row.