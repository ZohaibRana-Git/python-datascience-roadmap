# ============================================================
# Phase 1 | Topic 3: Functions
# ============================================================
# Function = reusable code block.
# Ek baar define karo, baar baar call karo.
# def keyword se function banate hain.
# ============================================================

# --- Basic Function ---
def greet():
    """Simple function — no parameters."""
    print("Hello! Python functions seekh rahe ho.")

greet()

# --- Function with Parameters ---
def greet_person(name):
    """Ek parameter leta hai."""
    print(f"Hello, {name}!")

greet_person("Ali")
greet_person("Sara")

# --- Return Value ---
def add(a, b):
    """Do numbers add karta hai aur result return karta hai."""
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# --- Default Parameters ---
def describe(name, age=18, city="Karachi"):
    """Default values — agar pass na karo to ye use hoti hain."""
    print(f"{name} | Age: {age} | City: {city}")

print("\n=== Default Parameters ===")
describe("Ali")                          # default age=18, city=Karachi
describe("Sara", age=25)                 # city default rahega
describe("Ahmed", age=30, city="Lahore") # sab override

# --- Multiple Return Values ---
def min_max(numbers):
    """List ka minimum aur maximum return karta hai."""
    return min(numbers), max(numbers)

data = [4, 7, 1, 9, 3, 6]
low, high = min_max(data)
print(f"\nData  : {data}")
print(f"Min   : {low}")
print(f"Max   : {high}")

# --- *args (variable number of arguments) ---
def total(*args):
    """Kitne bhi numbers pass karo — sab add kar dega."""
    return sum(args)

print(f"\ntotal(1,2,3)     = {total(1, 2, 3)}")
print(f"total(10,20,30,40) = {total(10, 20, 30, 40)}")

# --- **kwargs (keyword arguments) ---
def show_info(**kwargs):
    """Key-value pairs accept karta hai."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\n=== **kwargs ===")
show_info(name="Ali", age=22, job="Developer")

# --- Lambda Functions (anonymous / one-liner) ---
print("\n=== Lambda Functions ===")

square  = lambda x: x ** 2
add_two = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print(f"square(5)    = {square(5)}")
print(f"add_two(3,4) = {add_two(3, 4)}")
print(f"is_even(7)   = {is_even(7)}")

# Lambda with sorted()
students = [("Ali", 85), ("Sara", 92), ("Ahmed", 78)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(f"\nTop students: {sorted_students}")

# --- Nested Functions ---
def outer(x):
    """Function ke andar function."""
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(f"\nadd5(3) = {add5(3)}")   # 5 + 3 = 8
print(f"add5(10) = {add5(10)}")  # 5 + 10 = 15

# --- Recursive Function ---
def factorial(n):
    """n! = n × (n-1) × ... × 1  — recursion example."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\n=== Recursion ===")
for i in range(1, 7):
    print(f"  {i}! = {factorial(i)}")

# --- Practical: Data Science use case ---
def normalize(data):
    """
    Min-Max normalization — values ko 0 aur 1 ke beech le aata hai.
    Data Science me bahut use hota hai.
    """
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

raw = [10, 20, 30, 40, 50]
normalized = normalize(raw)
print(f"\n=== Normalization ===")
print(f"Raw        : {raw}")
print(f"Normalized : {[round(v, 2) for v in normalized]}")
