# ============================================================
# Phase 2 | Topic 5: Data Cleaning
# ============================================================
# Real-world data messy hoti hai — Data Science ka 60% kaam
# data clean karna hota hai.
# Missing values, duplicates, wrong types, outliers
# ============================================================

import pandas as pd
import numpy as np

# Messy dataset banao (real-world jaisa)
raw_data = {
    "name"  : ["Ali", "Sara", "Ahmed", None, "Bilal", "Sara", "Hina", "Omar"],
    "age"   : [22, 20, None, 21, 24, 20, 22, 999],    # 999 = outlier
    "score" : [85, 92, 78, 95, None, 92, 88, 72],
    "city"  : ["Karachi", "lahore", "Islamabad", "KARACHI", "Lahore", "lahore", None, "Islamabad"],
    "salary": ["50000", "75000", "60000", "80000", "55000", "75000", "70000", "65000"]
}

df = pd.DataFrame(raw_data)
print("=== Raw (Messy) Data ===")
print(df)

# ─────────────────────────────────────────
# 1. Missing Values Check
# ─────────────────────────────────────────
print("\n=== Missing Values ===")
print("Null counts:")
print(df.isnull().sum())
print(f"\nTotal nulls: {df.isnull().sum().sum()}")
print(f"Null %:\n{(df.isnull().sum() / len(df) * 100).round(1)}")

# ─────────────────────────────────────────
# 2. Handle Missing Values
# ─────────────────────────────────────────
print("\n=== Handle Missing Values ===")

# Numeric → mean/median se fill karo
df["age"]   = df["age"].fillna(df["age"].median())
df["score"] = df["score"].fillna(df["score"].mean())

# Categorical → mode ya "Unknown"
df["name"] = df["name"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")

print("After filling nulls:")
print(df.isnull().sum())

# ─────────────────────────────────────────
# 3. Duplicates
# ─────────────────────────────────────────
print("\n=== Duplicates ===")
print(f"Duplicate rows: {df.duplicated().sum()}")
print("Duplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()
print(f"After drop: {len(df)} rows")

# ─────────────────────────────────────────
# 4. Data Types Fix
# ─────────────────────────────────────────
print("\n=== Fix Data Types ===")
print(f"Before:\n{df.dtypes}")

df["salary"] = df["salary"].astype(int)    # string → int
df["age"]    = df["age"].astype(int)

print(f"\nAfter:\n{df.dtypes}")

# ─────────────────────────────────────────
# 5. String Cleaning
# ─────────────────────────────────────────
print("\n=== String Cleaning ===")
print(f"Cities before: {df['city'].unique()}")

df["city"] = df["city"].str.strip()         # whitespace remove
df["city"] = df["city"].str.title()         # Title Case
df["name"] = df["name"].str.strip().str.title()

print(f"Cities after : {df['city'].unique()}")

# ─────────────────────────────────────────
# 6. Outlier Detection & Removal
# ─────────────────────────────────────────
print("\n=== Outliers (IQR Method) ===")
print(f"Age before: {df['age'].values}")

Q1  = df["age"].quantile(0.25)
Q3  = df["age"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f"Q1={Q1}, Q3={Q3}, IQR={IQR}")
print(f"Valid range: {lower:.1f} – {upper:.1f}")

outliers = df[(df["age"] < lower) | (df["age"] > upper)]
print(f"Outliers:\n{outliers[['name','age']]}")

df = df[(df["age"] >= lower) & (df["age"] <= upper)]
print(f"After removing outliers: {len(df)} rows")

# ─────────────────────────────────────────
# 7. Final Clean Data
# ─────────────────────────────────────────
print("\n=== Final Clean Data ===")
df = df.reset_index(drop=True)
print(df)
print(f"\nShape: {df.shape}")
print(f"Nulls: {df.isnull().sum().sum()}")
