# Python Basics — Learning Project

Yeh project Python ke fundamentals seekhne ke liye banaya gaya hai. Har topic ek alag file mein hai, aur `main.py` sab ko ek saath run karta hai.

---

## Project Structure

```
python-basics/
├── main.py              # Sab modules ko import karke run karta hai
├── variables.py         # Variables aur data types
├── loops.py             # For loop aur while loop
├── functions.py         # Functions, parameters, return values
├── data_structures.py   # Lists aur Dictionaries
├── file_handling.py     # File read/write karna
└── data/
    ├── sample.txt       # Reading ke liye sample file
    └── output.txt       # Program run karne par banta hai
```

---

## Requirements

- Python 3.x installed hona chahiye
- Koi extra library install karne ki zaroorat nahi

Python version check karne ke liye:
```bash
python --version
```

---

## Project Kaise Run Karein

```bash
cd python-basics
python main.py
```

Yeh command sab topics ke examples ek saath print karega.

---

## Topics

### 1. Variables — `variables.py`

Python mein variables ko declare karne ki zaroorat nahi hoti. Seedha value assign karo.

| Data Type | Example         | Description          |
|-----------|-----------------|----------------------|
| `str`     | `"Alice"`       | Text / string        |
| `int`     | `25`            | Pura number          |
| `float`   | `5.7`           | Decimal number       |
| `bool`    | `True / False`  | Haan ya Nahi         |

```python
name = "Alice"        # string
age = 25              # integer
height = 5.7          # float
is_student = True     # boolean

print(f"{name} is {age} years old.")
# Output: Alice is 25 years old.
```

---

### 2. Loops — `loops.py`

Loops se ek kaam baar baar kiya ja sakta hai.

**For Loop** — jab pata ho kitni baar chalana hai:
```python
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

**While Loop** — jab ek condition ke basis par chalna ho:
```python
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
# Output: 1 2 3 4 5
```

---

### 3. Functions — `functions.py`

Functions reusable code blocks hote hain. `def` keyword se banate hain.

```python
# Simple function
def greet():
    print("Hello!")

# Parameter wali function
def greet_person(name):
    print(f"Hello, {name}!")

# Return value wali function
def add_numbers(a, b):
    return a + b

result = add_numbers(7, 3)
print(result)  # Output: 10
```

**Default Parameter:**
```python
def describe_person(name, age=18):
    print(f"{name} is {age} years old.")

describe_person("Charlie")       # age default = 18
describe_person("Diana", age=30) # age override = 30
```

---

### 4. Data Structures — `data_structures.py`

**List** — ordered collection of items:
```python
colors = ["red", "green", "blue"]

colors.append("yellow")   # add karo
colors.remove("green")    # hatao
print(colors[0])          # pehla item: red

for color in colors:
    print(color)
```

**Dictionary** — key-value pairs:
```python
person = {"name": "Eve", "age": 28}

print(person["name"])     # Eve
person["city"] = "Karachi"  # naya key add karo

for key, value in person.items():
    print(f"{key}: {value}")
```

---

### 5. File Handling — `file_handling.py`

Python mein files ke saath kaam karna bahut aasaan hai.

**File Padhna:**
```python
with open("data/sample.txt", "r") as file:
    content = file.read()
    print(content)
```

**File Likhna** (purana content hat jata hai):
```python
with open("data/output.txt", "w") as file:
    file.write("Yeh Python ne likha hai!\n")
```

**File mein Add Karna** (purana content rehta hai):
```python
with open("data/output.txt", "a") as file:
    file.write("Yeh line baad mein add ki gayi.\n")
```

> `with` statement use karo — file automatically band ho jati hai.

---

### 6. main.py — Sab Ek Saath

```python
from variables import show_variables
from loops import show_for_loop, show_while_loop
from functions import show_functions
from data_structures import show_data_structures
from file_handling import show_file_handling

def main():
    show_variables()
    show_for_loop()
    show_while_loop()
    show_functions()
    show_data_structures()
    show_file_handling()

if __name__ == "__main__":
    main()
```

---

## Expected Output (Sample)

```
=============================================
   Python Basics — Learning Project
=============================================

=== Variables & Data Types ===
Name    : Alice  -> type: <class 'str'>
Age     : 25     -> type: <class 'int'>
...

=== For Loop ===
  Step 0
  Step 1
  ...

=== Functions ===
Hello! Welcome to Python functions.
7 + 3 = 10
...

=============================================
   All topics complete. Happy coding!
=============================================
```

---

## Aage Seekhne Ke Liye

Yeh project complete karne ke baad in topics ko explore karo:

- `if / elif / else` — conditions
- `classes` aur `objects` — Object Oriented Programming
- `modules` aur `pip` — external libraries
- `error handling` — try / except
- `list comprehensions` — short aur clean loops
