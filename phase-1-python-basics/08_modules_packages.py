# ============================================================
# Phase 1 | Topic 8: Modules & Packages
# ============================================================
# Module = ek Python file jisme functions/classes hain
# Package = modules ka collection (folder with __init__.py)
# Built-in modules: os, math, random, datetime, collections
# ============================================================

import os
import math
import random
import datetime
from collections import Counter, defaultdict

# ─────────────────────────────────────────
# 1. os module — file system operations
# ─────────────────────────────────────────
print("=== os module ===")
print(f"  Current dir  : {os.getcwd()}")
print(f"  Path exists  : {os.path.exists('data')}")
print(f"  Join paths   : {os.path.join('data', 'file.csv')}")
print(f"  Basename     : {os.path.basename('/home/user/data.csv')}")
print(f"  Dirname      : {os.path.dirname('/home/user/data.csv')}")

# ─────────────────────────────────────────
# 2. math module
# ─────────────────────────────────────────
print("\n=== math module ===")
print(f"  sqrt(144)    = {math.sqrt(144)}")
print(f"  pi           = {math.pi:.5f}")
print(f"  ceil(4.2)    = {math.ceil(4.2)}")
print(f"  floor(4.9)   = {math.floor(4.9)}")
print(f"  log(100, 10) = {math.log(100, 10)}")
print(f"  factorial(6) = {math.factorial(6)}")

# ─────────────────────────────────────────
# 3. random module — Data Science me sampling ke liye
# ─────────────────────────────────────────
print("\n=== random module ===")
random.seed(42)   # seed set karo — reproducible results

print(f"  random()          = {random.random():.4f}")       # 0.0 to 1.0
print(f"  randint(1,100)    = {random.randint(1, 100)}")    # inclusive
print(f"  choice(list)      = {random.choice(['a','b','c','d'])}")

data = list(range(1, 11))
random.shuffle(data)
print(f"  shuffle([1..10])  = {data}")
print(f"  sample(5)         = {random.sample(data, 5)}")    # 5 unique items

# ─────────────────────────────────────────
# 4. datetime module
# ─────────────────────────────────────────
print("\n=== datetime module ===")
now   = datetime.datetime.now()
today = datetime.date.today()

print(f"  Now   : {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Today : {today}")
print(f"  Year  : {now.year}")

# Date difference
start = datetime.date(2025, 1, 1)
end   = datetime.date(2025, 12, 31)
diff  = end - start
print(f"  Days in 2025: {diff.days}")

# ─────────────────────────────────────────
# 5. collections module — Data Science me useful
# ─────────────────────────────────────────
print("\n=== collections.Counter ===")
words  = ["python", "data", "python", "science", "data", "python", "ml"]
counts = Counter(words)
print(f"  Counts      : {dict(counts)}")
print(f"  Most common : {counts.most_common(2)}")

scores = [85, 92, 78, 85, 95, 92, 85, 78]
score_count = Counter(scores)
print(f"\n  Score freq  : {dict(score_count)}")

print("\n=== collections.defaultdict ===")
# Normal dict me missing key → KeyError
# defaultdict me missing key → default value
city_students = defaultdict(list)
city_students["Karachi"].append("Ali")
city_students["Karachi"].append("Zara")
city_students["Lahore"].append("Sara")
city_students["Islamabad"].append("Ahmed")

for city, students in city_students.items():
    print(f"  {city:12}: {students}")

# ─────────────────────────────────────────
# 6. Practical: Generate fake dataset
# ─────────────────────────────────────────
print("\n=== Practical: Generate Sample Dataset ===")

random.seed(0)
names  = ["Ali", "Sara", "Ahmed", "Zara", "Bilal", "Hina", "Omar", "Ayesha"]
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar"]

dataset = []
for i in range(8):
    record = {
        "id"    : i + 1,
        "name"  : names[i],
        "age"   : random.randint(20, 30),
        "score" : random.randint(60, 100),
        "city"  : random.choice(cities)
    }
    dataset.append(record)

print(f"  {'ID':<4} {'Name':<10} {'Age':<5} {'Score':<7} {'City'}")
print(f"  {'-'*40}")
for r in dataset:
    print(f"  {r['id']:<4} {r['name']:<10} {r['age']:<5} {r['score']:<7} {r['city']}")

avg_score = sum(r["score"] for r in dataset) / len(dataset)
print(f"\n  Average Score: {avg_score:.1f}")
