# ============================================================
# Phase 1 | Topic 7: Error Handling
# ============================================================
# Program crash na ho — errors ko gracefully handle karo.
# try / except / else / finally
# ============================================================

# ─────────────────────────────────────────
# 1. Basic try-except
# ─────────────────────────────────────────
print("=== Basic try-except ===")

try:
    result = 10 / 0          # ZeroDivisionError
except ZeroDivisionError:
    print("  Error: Zero se divide nahi kar sakte!")

# ─────────────────────────────────────────
# 2. Multiple Exceptions
# ─────────────────────────────────────────
print("\n=== Multiple Exceptions ===")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  Zero division!")
        return None
    except TypeError:
        print("  Type error — numbers pass karo!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "x"))

# ─────────────────────────────────────────
# 3. else aur finally
# ─────────────────────────────────────────
print("\n=== else + finally ===")

def read_number(value):
    try:
        num = int(value)
    except ValueError:
        print(f"  '{value}' → integer nahi hai!")
    else:
        # try successful hone par chalta hai
        print(f"  '{value}' → integer: {num}")
    finally:
        # hamesha chalta hai — cleanup ke liye
        print("  (finally block always runs)")

read_number("42")
read_number("hello")

# ─────────────────────────────────────────
# 4. Exception object se message lena
# ─────────────────────────────────────────
print("\n=== Exception Message ===")

try:
    my_list = [1, 2, 3]
    print(my_list[10])       # IndexError
except IndexError as e:
    print(f"  IndexError: {e}")

try:
    data = {"name": "Ali"}
    print(data["age"])       # KeyError
except KeyError as e:
    print(f"  KeyError: {e} key nahi mili")

# ─────────────────────────────────────────
# 5. Custom Exception
# ─────────────────────────────────────────
print("\n=== Custom Exception ===")

class InvalidScoreError(Exception):
    """Score 0-100 ke bahar ho to ye raise hoti hai."""
    pass

def set_score(score):
    if not (0 <= score <= 100):
        raise InvalidScoreError(f"Score {score} invalid! (0-100 hona chahiye)")
    print(f"  Score set: {score}")

try:
    set_score(85)
    set_score(150)   # ye error raise karega
except InvalidScoreError as e:
    print(f"  Custom Error: {e}")

# ─────────────────────────────────────────
# 6. Data Science Practical — Safe file read
# ─────────────────────────────────────────
print("\n=== Practical: Safe File Read ===")

import os

def read_dataset(filepath):
    """File safely read karta hai — crash nahi hoga."""
    try:
        with open(filepath, "r") as f:
            data = f.read()
            print(f"  File read: {len(data)} characters")
            return data
    except FileNotFoundError:
        print(f"  File nahi mili: {filepath}")
        return None
    except PermissionError:
        print(f"  Permission denied: {filepath}")
        return None

read_dataset("data/sample.txt")
read_dataset("data/nonexistent.csv")   # gracefully handle
