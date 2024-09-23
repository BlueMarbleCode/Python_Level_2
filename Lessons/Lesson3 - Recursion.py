#######################################
# The Blue Marble Academy
# Python Recursion – Introduction and Examples


# NOTE: Recursion happens when a function calls itself.
#       A recursive function must have a base case to stop,
#       otherwise it will keep calling itself forever.

#######################################
# Example 1: Factorial Function Using Recursion

# A factorial is the product of all positive integers less than or equal to a number.
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    # Base case: If n is 0, return 1 (since factorial(0) is 1)
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Test the factorial function
number = 5
print(f"Factorial of {number} is {factorial(number)}")

#######################################
# Example 2: Sum of Numbers Using Recursion

# A function to calculate the sum of natural numbers from 1 to n.
def sum_natural(n):
    # Base case: If n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: n + sum of numbers up to (n-1)
    return n + sum_natural(n - 1)

# Test the sum_natural function
n = 10
print(f"The sum of numbers from 1 to {n} is {sum_natural(n)}")

# Recursive functions must have a **base case** to stop the recursion. Without a base case,
# the function would continue calling itself infinitely, leading to an error.

#######################################
# **Recursive Countdown**: Write a recursive function `countdown(n)` that prints the numbers from n down to 1.
#   - Example: countdown(5) should print 5, 4, 3, 2, 1.

# **Sum of List**: Write a recursive function `sum_list(lst)` that returns the sum of all elements in a list.
#    - Example: sum_list([1, 2, 3, 4, 5]) should return 15.

# **Reverse a String**: Write a recursive function `reverse_string(s)` that returns the reverse of a string.
#    - Example: reverse_string("Blue") should return "eulB".
