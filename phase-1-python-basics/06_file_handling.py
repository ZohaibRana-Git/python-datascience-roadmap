# ============================================================
# Phase 1 | Topic 6: File Handling
# ============================================================
# Python se files read, write, aur append kar sakte hain.
# Data Science me CSV, TXT files bahut use hoti hain.
# Best practice: "with" statement use karo — auto close hoti hai.
# ============================================================

import os
import csv
import json

# Paths
DATA_DIR   = os.path.join(os.path.dirname(__file__), "data")
SAMPLE_TXT = os.path.join(DATA_DIR, "sample.txt")
OUTPUT_TXT = os.path.join(DATA_DIR, "output.txt")
CSV_FILE   = os.path.join(DATA_DIR, "students.csv")
JSON_FILE  = os.path.join(DATA_DIR, "config.json")

os.makedirs(DATA_DIR, exist_ok=True)   # data/ folder banao agar nahi hai

# ─────────────────────────────────────────
# 1. Write & Read — Text File
# ─────────────────────────────────────────
print("=== Write Text File ===")
with open(OUTPUT_TXT, "w") as f:
    f.write("Line 1: Python file handling\n")
    f.write("Line 2: Data Science ke liye important hai\n")
    f.write("Line 3: CSV aur JSON bhi seekhenge\n")
print(f"  Written to: {OUTPUT_TXT}")

print("\n=== Read Entire File ===")
with open(OUTPUT_TXT, "r") as f:
    content = f.read()
print(content)

print("=== Read Line by Line ===")
with open(OUTPUT_TXT, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

# ─────────────────────────────────────────
# 2. Append
# ─────────────────────────────────────────
print("\n=== Append to File ===")
with open(OUTPUT_TXT, "a") as f:
    f.write("Line 4: Append mode — existing content safe rehta hai\n")
print("  Line appended.")

# ─────────────────────────────────────────
# 3. CSV File — Data Science me bahut common
# ─────────────────────────────────────────
print("\n=== Write CSV ===")
students = [
    ["Name",  "Age", "Score", "City"],
    ["Ali",    22,    85,     "Karachi"],
    ["Sara",   20,    92,     "Lahore"],
    ["Ahmed",  23,    78,     "Islamabad"],
    ["Zara",   21,    95,     "Karachi"],
]

with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
print(f"  CSV written: {CSV_FILE}")

print("\n=== Read CSV ===")
with open(CSV_FILE, "r") as f:
    reader = csv.DictReader(f)   # DictReader → har row ek dict hoti hai
    for row in reader:
        print(f"  {row['Name']:8} | Score: {row['Score']} | City: {row['City']}")

# ─────────────────────────────────────────
# 4. JSON File — APIs aur configs ke liye
# ─────────────────────────────────────────
print("\n=== Write JSON ===")
config = {
    "project"  : "Data Science Roadmap",
    "version"  : "1.0",
    "author"   : "Ali",
    "phases"   : ["Python", "NumPy", "Pandas", "ML", "DL"],
    "settings" : {
        "debug"     : False,
        "max_epochs": 100,
        "lr"        : 0.001
    }
}

with open(JSON_FILE, "w") as f:
    json.dump(config, f, indent=4)   # indent=4 → readable format
print(f"  JSON written: {JSON_FILE}")

print("\n=== Read JSON ===")
with open(JSON_FILE, "r") as f:
    loaded = json.load(f)

print(f"  Project : {loaded['project']}")
print(f"  Phases  : {loaded['phases']}")
print(f"  LR      : {loaded['settings']['lr']}")

# ─────────────────────────────────────────
# 5. File Existence Check
# ─────────────────────────────────────────
print("\n=== File Checks ===")
for path in [OUTPUT_TXT, CSV_FILE, JSON_FILE]:
    exists = os.path.exists(path)
    size   = os.path.getsize(path) if exists else 0
    print(f"  {os.path.basename(path):15} exists={exists}  size={size} bytes")
