# ============================================================
# Phase 2 | Topic 3: Pandas Basics
# ============================================================
# Pandas = Python Data Analysis Library
# Series  → 1D labeled array (ek column)
# DataFrame → 2D table (rows + columns) — Excel jaisa
# pip install pandas
# ============================================================

import pandas as pd
import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

print("Pandas version:", pd.__version__)

# ─────────────────────────────────────────
# 1. Series
# ─────────────────────────────────────────
print("\n=== Series ===")

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([85, 92, 78, 95], index=["Ali", "Sara", "Ahmed", "Zara"])

print(f"Default index:\n{s1}\n")
print(f"Custom index:\n{s2}\n")
print(f"s2['Sara']  = {s2['Sara']}")
print(f"s2.mean()   = {s2.mean()}")
print(f"s2[s2 > 80] =\n{s2[s2 > 80]}")

# ─────────────────────────────────────────
# 2. DataFrame — Create karo
# ─────────────────────────────────────────
print("\n=== DataFrame ===")

data = {
    "name"  : ["Ali", "Sara", "Ahmed", "Zara", "Bilal", "Hina"],
    "age"   : [22, 20, 23, 21, 24, 22],
    "score" : [85, 92, 78, 95, 67, 88],
    "city"  : ["Karachi", "Lahore", "Islamabad", "Karachi", "Lahore", "Islamabad"],
    "passed": [True, True, True, True, False, True]
}

df = pd.DataFrame(data)
print(df)

# ─────────────────────────────────────────
# 3. Basic Info
# ─────────────────────────────────────────
print("\n=== Basic Info ===")
print(f"Shape  : {df.shape}")          # (rows, cols)
print(f"Columns: {list(df.columns)}")
print(f"dtypes :\n{df.dtypes}\n")

print("df.head(3):")
print(df.head(3))

print("\ndf.describe():")
print(df.describe())

print("\ndf.info():")
df.info()

# ─────────────────────────────────────────
# 4. Access Columns & Rows
# ─────────────────────────────────────────
print("\n=== Access Data ===")
print(f"Names column:\n{df['name'].values}")
print(f"\nScore column:\n{df['score'].values}")

# Multiple columns
print(f"\nName + Score:\n{df[['name','score']]}")

# Row by index — iloc (position), loc (label)
print(f"\nRow 0 (iloc):\n{df.iloc[0]}")
print(f"\nRows 1-3 (iloc):\n{df.iloc[1:4]}")

# ─────────────────────────────────────────
# 5. CSV Read / Write
# ─────────────────────────────────────────
csv_path = os.path.join(DATA_DIR, "students.csv")

print("\n=== Save to CSV ===")
df.to_csv(csv_path, index=False)
print(f"  Saved: {csv_path}")

print("\n=== Read from CSV ===")
df_loaded = pd.read_csv(csv_path)
print(df_loaded)

# ─────────────────────────────────────────
# 6. Add / Remove Columns
# ─────────────────────────────────────────
print("\n=== Add / Remove Columns ===")
df["grade"] = df["score"].apply(lambda s: "A" if s >= 90 else ("B" if s >= 75 else "C"))
df["score_normalized"] = ((df["score"] - df["score"].min()) /
                          (df["score"].max() - df["score"].min())).round(2)

print(df[["name", "score", "grade", "score_normalized"]])

df_clean = df.drop(columns=["score_normalized"])
print(f"\nAfter drop: {list(df_clean.columns)}")
