# ============================================================
# Phase 1 | Topic 2: Loops
# ============================================================
# Loops same kaam baar baar karne ke liye use hote hain.
# Python me 2 types hain: for loop aur while loop.
# ============================================================

# --- For Loop: range() ---
print("=== For Loop: range() ===")

for i in range(5):          # 0, 1, 2, 3, 4
    print(f"  i = {i}")

print()
for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(f"  count = {i}")

print()
for i in range(0, 20, 5):   # 0, 5, 10, 15  (step = 5)
    print(f"  step = {i}")

# --- For Loop: list ke upar ---
print("\n=== For Loop: List ===")
fruits = ["apple", "banana", "mango", "grape"]

for fruit in fruits:
    print(f"  - {fruit}")

# enumerate() → index bhi milta hai
print("\nWith index:")
for index, fruit in enumerate(fruits):
    print(f"  [{index}] {fruit}")

# --- For Loop: string ke upar ---
print("\n=== For Loop: String ===")
word = "Python"
for char in word:
    print(f"  {char}")

# --- While Loop ---
print("\n=== While Loop ===")
counter = 1
while counter <= 5:
    print(f"  counter = {counter}")
    counter += 1   # counter = counter + 1

# --- break aur continue ---
print("\n=== break ===")
for i in range(10):
    if i == 5:
        print("  5 pe rok diya!")
        break       # loop band kar do
    print(f"  {i}")

print("\n=== continue ===")
for i in range(10):
    if i % 2 == 0:
        continue    # even numbers skip karo
    print(f"  odd: {i}")

# --- Nested Loops ---
print("\n=== Nested Loops (Multiplication Table) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")
    print()

# --- List Comprehension (Pythonic shortcut) ---
print("=== List Comprehension ===")

# Normal loop
squares_normal = []
for i in range(1, 6):
    squares_normal.append(i ** 2)

# Comprehension — same kaam ek line me
squares = [i ** 2 for i in range(1, 6)]
evens   = [i for i in range(20) if i % 2 == 0]

print(f"Squares : {squares}")
print(f"Evens   : {evens}")

# --- Practical Example: Sum of list ---
print("\n=== Practical: Sum without sum() ===")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers : {numbers}")
print(f"Total   : {total}")
