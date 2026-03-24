# data_structures.py
# ==================
# Python has powerful built-in data structures.
# Here we cover two of the most important ones:
#   - List: an ordered collection of items
#   - Dictionary: a collection of key-value pairs


def show_lists():
    """Demonstrates Python lists."""

    print("=== Lists ===")

    # Creating a list — items are in square brackets
    colors = ["red", "green", "blue", "yellow"]
    print(f"Colors list: {colors}")

    # Accessing items by index (index starts at 0)
    print(f"First color : {colors[0]}")
    print(f"Last color  : {colors[-1]}")  # -1 means the last item

    # Adding an item to the end of the list
    colors.append("purple")
    print(f"After append: {colors}")

    # Removing an item by value
    colors.remove("green")
    print(f"After remove: {colors}")

    # Looping through a list
    print("All colors:")
    for color in colors:
        print(f"  - {color}")

    # List length
    print(f"Total colors: {len(colors)}")


def show_dictionaries():
    """Demonstrates Python dictionaries."""

    print("\n=== Dictionaries ===")

    # Creating a dictionary — key: value pairs in curly braces
    person = {
        "name": "Eve",
        "age": 28,
        "city": "New York"
    }
    print(f"Person dict: {person}")

    # Accessing a value by its key
    print(f"Name: {person['name']}")
    print(f"Age : {person['age']}")

    # Adding a new key-value pair
    person["job"] = "Developer"
    print(f"After adding job: {person}")

    # Updating an existing value
    person["age"] = 29
    print(f"After birthday : {person}")

    # Looping through keys and values
    print("Person details:")
    for key, value in person.items():
        print(f"  {key}: {value}")

    # Check if a key exists
    if "city" in person:
        print(f"City is: {person['city']}")


def show_data_structures():
    """Runs all data structure examples."""
    show_lists()
    show_dictionaries()
