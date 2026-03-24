# ============================================================
# Phase 1 | Topic 1: Variables & Data Types
# ============================================================
# Variable = ek container jisme data store hota hai.
# Python me type automatically detect hoti hai (dynamic typing).
# ============================================================

# --- Basic Data Types ---

name       = "Ali"        # str   → text
age        = 22           # int   → whole number
height     = 5.9          # float → decimal number
is_student = True         # bool  → True ya False

print("=== Basic Variables ===")
print(f"Name    : {name}  ({type(name).__name__})")
print(f"Age     : {age}   ({type(age).__name__})")
print(f"Height  : {height} ({type(height).__name__})")
print(f"Student : {is_student} ({type(is_student).__name__})")

# --- Type Conversion ---
print("\n=== Type Conversion ===")

age_str   = str(age)        # int → string
price_int = int(99.9)       # float → int (decimal cut hoti hai)
num_float = float("3.14")   # string → float

print(f"str(22)      = '{age_str}'  type: {type(age_str).__name__}")
print(f"int(99.9)    = {price_int}   type: {type(price_int).__name__}")
print(f"float('3.14')= {num_float}  type: {type(num_float).__name__}")

# --- String Operations ---
print("\n=== String Operations ===")

full_name = "Ali Khan"
print(f"Upper     : {full_name.upper()}")
print(f"Lower     : {full_name.lower()}")
print(f"Length    : {len(full_name)}")
print(f"Replace   : {full_name.replace('Ali', 'Ahmed')}")
print(f"Split     : {full_name.split(' ')}")
print(f"Starts w/ : {full_name.startswith('Ali')}")

# --- Multiple Assignment ---
print("\n=== Multiple Assignment ===")
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

a = b = c = 100   # sab ko same value
print(f"a={a}, b={b}, c={c}")

# --- Constants (convention: UPPER_CASE) ---
PI        = 3.14159
MAX_SCORE = 100
print(f"\nPI = {PI}, MAX_SCORE = {MAX_SCORE}")

# --- None Type ---
result = None   # koi value nahi — jaise null in other languages
print(f"\nresult = {result}, type = {type(result).__name__}")

# --- Arithmetic Operators ---
print("\n=== Arithmetic ===")
print(f"10 + 3  = {10 + 3}")
print(f"10 - 3  = {10 - 3}")
print(f"10 * 3  = {10 * 3}")
print(f"10 / 3  = {10 / 3:.2f}")   # float division
print(f"10 // 3 = {10 // 3}")      # floor division
print(f"10 % 3  = {10 % 3}")       # remainder (modulus)
print(f"2 ** 8  = {2 ** 8}")       # power (2 to the 8)
