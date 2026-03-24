# functions.py
# ============
# Functions are reusable blocks of code.
# You define a function once and call it as many times as you need.
# Use the "def" keyword to define a function.


def greet():
    """A simple function with no parameters."""
    # This function just prints a greeting
    print("Hello! Welcome to Python functions.")


def greet_person(name):
    """A function that takes one parameter."""
    # 'name' is a parameter — a value passed into the function
    print(f"Hello, {name}! Nice to meet you.")


def add_numbers(a, b):
    """A function that takes two numbers and returns their sum."""
    result = a + b
    return result  # 'return' sends a value back to the caller


def describe_person(name, age=18):
    """
    A function with a default parameter.
    If 'age' is not provided, it defaults to 18.
    """
    print(f"{name} is {age} years old.")


def get_square_and_cube(number):
    """A function that returns multiple values."""
    square = number ** 2   # ** means "to the power of"
    cube = number ** 3
    return square, cube    # Python can return multiple values as a tuple


def show_functions():
    """Runs all function examples."""

    print("=== Functions ===")

    # Calling a simple function
    greet()

    # Passing an argument to a function
    greet_person("Bob")

    # Using the return value of a function
    total = add_numbers(7, 3)
    print(f"7 + 3 = {total}")

    # Using default parameter
    describe_person("Charlie")          # uses default age = 18
    describe_person("Diana", age=30)    # overrides the default

    # Unpacking multiple return values
    sq, cu = get_square_and_cube(4)
    print(f"4 squared = {sq}, 4 cubed = {cu}")
