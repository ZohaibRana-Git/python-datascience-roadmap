# main.py
# =======
# This is the entry point of the project.
# It imports and runs examples from every module so you can see
# all topics in action with a single command: python main.py

# Import the example functions from each module
from variables import show_variables
from loops import show_for_loop, show_while_loop
from functions import show_functions
from data_structures import show_data_structures
from file_handling import show_file_handling


def main():
    """Runs all topic examples in order."""

    print("=" * 45)
    print("   Python Basics — Learning Project")
    print("=" * 45)
    print()

    # --- Topic 1: Variables ---
    show_variables()
    print()

    # --- Topic 2: Loops ---
    show_for_loop()
    show_while_loop()
    print()

    # --- Topic 3: Functions ---
    show_functions()
    print()

    # --- Topic 4: Data Structures ---
    show_data_structures()
    print()

    # --- Topic 5: File Handling ---
    show_file_handling()
    print()

    print("=" * 45)
    print("   All topics complete. Happy coding!")
    print("=" * 45)


# This block ensures main() only runs when you execute this file directly.
# If another file imports main.py, this block is skipped.
if __name__ == "__main__":
    main()
