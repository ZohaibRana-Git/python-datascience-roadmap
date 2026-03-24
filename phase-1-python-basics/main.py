# ============================================================
# Phase 1 — Main Entry Point
# Sab topics ek saath run karne ke liye:  python main.py
# Ya individual file:  python 01_variables.py
# ============================================================

import subprocess
import sys
import os

topics = [
    ("01_variables.py",       "Variables & Data Types"),
    ("02_loops.py",           "Loops"),
    ("03_functions.py",       "Functions"),
    ("04_data_structures.py", "Data Structures"),
    ("05_oop.py",             "OOP — Classes & Objects"),
    ("06_file_handling.py",   "File Handling"),
    ("07_error_handling.py",  "Error Handling"),
    ("08_modules_packages.py","Modules & Packages"),
]

def run_topic(filename, title):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)
    path = os.path.join(os.path.dirname(__file__), filename)
    subprocess.run([sys.executable, path], check=True)

if __name__ == "__main__":
    print("=" * 55)
    print("   PHASE 1 — Python Basics")
    print("   Data Science Roadmap")
    print("=" * 55)

    for filename, title in topics:
        run_topic(filename, title)

    print("\n" + "=" * 55)
    print("   Phase 1 Complete! Next: Phase 2 — NumPy & Pandas")
    print("=" * 55)
