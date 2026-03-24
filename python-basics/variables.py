# variables.py
# ============
# In Python, variables are used to store data.
# You don't need to declare a type — Python figures it out automatically.
# This is called "dynamic typing".

# --- Data Types ---

# String: text wrapped in quotes
name = "Alice"

# Integer: whole numbers
age = 25

# Float: decimal numbers
height = 5.7

# Boolean: True or False (capital T and F)
is_student = True


def show_variables():
    """Prints all variable examples with their types."""

    print("=== Variables & Data Types ===")

    # type() tells you what kind of data a variable holds
    print(f"Name    : {name}  -> type: {type(name)}")
    print(f"Age     : {age}   -> type: {type(age)}")
    print(f"Height  : {height} -> type: {type(height)}")
    print(f"Student : {is_student} -> type: {type(is_student)}")

    # You can also do simple math with variables
    birth_year = 2026 - age
    print(f"\n{name} was born around: {birth_year}")

    # String concatenation (joining strings)
    greeting = "Hello, " + name + "!"
    print(greeting)

    # f-strings make it easy to embed variables inside strings
    print(f"{name} is {age} years old and {height}ft tall.")
