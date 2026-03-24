# ============================================================
# Phase 1 | Topic 4: Data Structures
# ============================================================
# Python ke 4 main built-in data structures:
#   List      → ordered, mutable, duplicates allowed
#   Tuple     → ordered, immutable (change nahi ho sakta)
#   Set       → unordered, unique values only
#   Dictionary→ key-value pairs
# ============================================================

# ─────────────────────────────────────────
# 1. LIST
# ─────────────────────────────────────────
print("=" * 40)
print("LIST")
print("=" * 40)

fruits = ["apple", "banana", "mango", "apple"]

# Access
print(f"First  : {fruits[0]}")
print(f"Last   : {fruits[-1]}")
print(f"Slice  : {fruits[1:3]}")   # index 1 aur 2

# Modify
fruits.append("grape")             # end me add
fruits.insert(1, "cherry")         # index 1 pe insert
fruits.remove("apple")             # pehla "apple" remove
popped = fruits.pop()              # last item remove aur return
print(f"After changes : {fruits}")
print(f"Popped item   : {popped}")

# Useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal : {numbers}")
print(f"Sorted   : {sorted(numbers)}")          # naya sorted list
print(f"Reversed : {list(reversed(numbers))}")  # naya reversed list
print(f"Count 1  : {numbers.count(1)}")         # kitni baar 1 aaya
print(f"Max      : {max(numbers)}")
print(f"Min      : {min(numbers)}")
print(f"Sum      : {sum(numbers)}")

# List of lists (2D — matrix jaisa)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix[1][2] = {matrix[1][2]}")   # row 1, col 2 = 6

# ─────────────────────────────────────────
# 2. TUPLE
# ─────────────────────────────────────────
print("\n" + "=" * 40)
print("TUPLE")
print("=" * 40)

# Tuple immutable hota hai — change nahi kar sakte
coordinates = (28.6139, 77.2090)   # Delhi lat/long
rgb = (255, 128, 0)

print(f"Coordinates : {coordinates}")
print(f"Latitude    : {coordinates[0]}")
print(f"RGB Red     : {rgb[0]}")

# Tuple unpacking
lat, lon = coordinates
print(f"Lat={lat}, Lon={lon}")

# Tuple as function return (already dekha functions me)
def get_stats(data):
    return min(data), max(data), sum(data) / len(data)

lo, hi, avg = get_stats([10, 20, 30, 40, 50])
print(f"\nMin={lo}, Max={hi}, Avg={avg}")

# ─────────────────────────────────────────
# 3. SET
# ─────────────────────────────────────────
print("\n" + "=" * 40)
print("SET")
print("=" * 40)

# Set me duplicates nahi hote — unique values only
tags = {"python", "data", "python", "science", "data"}
print(f"Set (unique) : {tags}")   # duplicates automatically remove

# Add / Remove
tags.add("ml")
tags.discard("data")   # error nahi deta agar item nahi
print(f"After update : {tags}")

# Set operations — Data Science me useful
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nA           : {set_a}")
print(f"B           : {set_b}")
print(f"Union       : {set_a | set_b}")         # dono mila ke
print(f"Intersection: {set_a & set_b}")         # common elements
print(f"Difference  : {set_a - set_b}")         # A me hai, B me nahi
print(f"Sym Diff    : {set_a ^ set_b}")         # sirf ek me hain

# ─────────────────────────────────────────
# 4. DICTIONARY
# ─────────────────────────────────────────
print("\n" + "=" * 40)
print("DICTIONARY")
print("=" * 40)

person = {
    "name"  : "Ali",
    "age"   : 22,
    "city"  : "Karachi",
    "skills": ["Python", "SQL", "Excel"]
}

# Access
print(f"Name   : {person['name']}")
print(f"Skills : {person['skills']}")
print(f"get()  : {person.get('salary', 'Not found')}")  # safe access

# Modify
person["age"]    = 23              # update
person["salary"] = 80000           # add new key
del person["city"]                 # delete key
print(f"\nUpdated: {person}")

# Loop through
print("\nAll key-value pairs:")
for key, value in person.items():
    print(f"  {key:10} → {value}")

# Keys, Values
print(f"\nKeys   : {list(person.keys())}")
print(f"Values : {list(person.values())}")

# Nested Dictionary
employees = {
    "E001": {"name": "Ali",   "dept": "Data",    "salary": 90000},
    "E002": {"name": "Sara",  "dept": "ML",      "salary": 120000},
    "E003": {"name": "Ahmed", "dept": "Backend", "salary": 85000},
}

print("\n=== Nested Dict ===")
for emp_id, info in employees.items():
    print(f"  {emp_id}: {info['name']} | {info['dept']} | {info['salary']}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares}")

# ─────────────────────────────────────────
# 5. WHEN TO USE WHAT?
# ─────────────────────────────────────────
print("\n=== When to Use What? ===")
print("  List       → ordered data, duplicates ok  e.g. [scores, names]")
print("  Tuple      → fixed data, coordinates, DB rows")
print("  Set        → unique items, fast lookup, deduplication")
print("  Dictionary → labeled data, JSON-like, fast key lookup")
