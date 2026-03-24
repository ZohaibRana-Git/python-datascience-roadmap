# file_handling.py
# ================
# Python makes it easy to read from and write to files.
# The built-in open() function is used to work with files.
# Best practice: use the "with" statement so the file closes automatically.

import os

# Path to our sample file (relative to this script's location)
SAMPLE_FILE = os.path.join(os.path.dirname(__file__), "data", "sample.txt")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "data", "output.txt")


def read_file():
    """Reads and prints the contents of sample.txt."""

    print("=== Reading a File ===")

    # 'r' mode means read-only
    # The 'with' block ensures the file is closed after we're done
    with open(SAMPLE_FILE, "r") as file:
        content = file.read()   # reads the entire file as one string
        print(content)


def read_file_line_by_line():
    """Reads a file one line at a time."""

    print("=== Reading Line by Line ===")

    with open(SAMPLE_FILE, "r") as file:
        # readlines() returns a list where each item is one line
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        # strip() removes the newline character at the end of each line
        print(f"  Line {i}: {line.strip()}")


def write_file():
    """Writes new content to output.txt."""

    print("\n=== Writing to a File ===")

    # 'w' mode means write — it creates the file if it doesn't exist,
    # or overwrites it if it does
    with open(OUTPUT_FILE, "w") as file:
        file.write("This file was created by Python!\n")
        file.write("File handling is easy with the 'with' statement.\n")

    print(f"  File written to: {OUTPUT_FILE}")


def append_to_file():
    """Appends a line to the existing output.txt."""

    print("\n=== Appending to a File ===")

    # 'a' mode means append — adds to the end without erasing existing content
    with open(OUTPUT_FILE, "a") as file:
        file.write("This line was appended later.\n")

    print("  Line appended successfully.")

    # Read it back to confirm
    print("  Updated file contents:")
    with open(OUTPUT_FILE, "r") as file:
        print(file.read())


def show_file_handling():
    """Runs all file handling examples."""
    read_file()
    print()
    read_file_line_by_line()
    write_file()
    append_to_file()
