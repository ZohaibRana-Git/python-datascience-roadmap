# loops.py
# ========
# Loops let you repeat a block of code multiple times.
# Python has two main types: for loops and while loops.


def show_for_loop():
    """Demonstrates the for loop using range()."""

    print("=== For Loop ===")

    # range(5) generates numbers 0, 1, 2, 3, 4
    # The loop runs once for each number
    for i in range(5):
        print(f"  Step {i}")

    print()

    # range(start, stop) — starts at 1, stops before 6
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(f"  Count: {i}")

    print()

    # Looping over a list of items directly
    fruits = ["apple", "banana", "cherry"]
    print("Fruits in the list:")
    for fruit in fruits:
        print(f"  - {fruit}")


def show_while_loop():
    """Demonstrates the while loop with a counter."""

    print("\n=== While Loop ===")

    # A while loop keeps running as long as the condition is True
    counter = 1

    while counter <= 5:
        print(f"  Counter is: {counter}")
        counter += 1  # Same as: counter = counter + 1

    print("  Loop finished!")

    print()

    # Practical example: keep asking until a condition is met
    # (simulated here without real input for demo purposes)
    number = 10
    print("Counting down from 10:")
    while number > 0:
        print(f"  {number}...")
        number -= 2  # Decrease by 2 each time
    print("  Blastoff!")
