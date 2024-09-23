#######################################
# The Blue Marble Academy
# Python Classes – Introduction and Examples

# NOTE: A class is like a blueprint for creating objects (instances).
#       An object has attributes (variables) and methods (functions).
#       Classes help organize code and model real-world things.

#######################################
# Example 1: Basic Class with an __init__ Method

# The `__init__` method is a special method called a constructor.
# It initializes the object's attributes when a new object is created.

class Dog:
    def __init__(self, name, breed):
        # Attributes of the class
        self.name = name
        self.breed = breed

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says: Woof!")

# Create an instance of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
print(f"The dog's name is {dog1.name} and it's a {dog1.breed}")
dog1.bark()  # Call the bark method

#######################################
# Example 2: Class with Methods

# We can add more methods to a class to define the behaviors of the object.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        self.is_running = True
        print(f"{self.make} {self.model} is now running.")

    # Method to stop the car
    def stop(self):
        self.is_running = False
        print(f"{self.make} {self.model} is now stopped.")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")
my_car.start()  # Start the car
my_car.stop()   # Stop the car

#######################################
# Example 3: Class with a Method that Takes Parameters

# We can create methods that take arguments to perform more specific tasks.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate the area of the rectangle
    def area(self):
        return self.width * self.height

# Create a rectangle instance
rect1 = Rectangle(10, 5)
print(f"The area of the rectangle is: {rect1.area()}")

#######################################
# Exercises:
#
# 1. **Create a Class**:
#    - Create a class called `Student` with attributes: name, age, and grade.
#    - Add a method `introduce()` that prints the student's name and age.
#
# 2. **Bank Account Class**:
#    - Create a class called `BankAccount` with attributes: `owner` and `balance`.
#    - Add methods to deposit, withdraw, and check the balance.
#    - Example: `account1.withdraw(50)` should reduce the balance by 50.
#
# 3. **Rectangle with Perimeter**:
#    - Modify the `Rectangle` class to add a method that calculates the perimeter of the rectangle.
