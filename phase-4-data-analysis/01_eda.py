# ============================================================
# Phase 4 | Topic 1: Exploratory Data Analysis (EDA)
# ============================================================
# Kisi bhi Data Science project me pehla kaam EDA hota hai.
# Data ko samjho — phir model banao.
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ─────────────────────────────────────────
# Sample Dataset Generate karo
# ─────────────────────────────────────────
n = 200
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
depts  = ["Data Science", "Machine Learning", "Backend", "Frontend"]

df = pd.DataFrame({
    "name"      : [f"Employee_{i}" for i in range(1, n+1)],
    "age"       : np.random.randint(22, 45, n),
    "experience": np.random.randint(0, 15, n),
    "salary"    : np.random.randint(50000, 300000, n),
    "score"     : np.random.randint(60, 100, n),
    "city"      : np.random.choice(cities, n),
    "dept"      : np.random.choice(depts, n),
})

# Kuch nulls inject karo (real-world jaisa)
df.loc[np.random.choice(n, 10, replace=False), "salary"] = np.nan
df.loc[np.random.choice(n, 5,  replace=False), "age"]    = np.nan

print("=" * 50)
print("STEP 1: Basic Info")
print("=" * 50)
print(f"Shape   : {df.shape}")
print(f"Columns : {list(df.columns)}")
print(f"\nFirst 5 rows:")
print(df.head())

print("\n" + "=" * 50)
print("STEP 2: Data Types & Nulls")
print("=" * 50)
df.info()
print(f"\nNull counts:\n{df.isnull().sum()}")
print(f"\nNull %:\n{(df.isnull().sum()/len(df)*100).round(2)}")

print("\n" + "=" * 50)
print("STEP 3: Statistical Summary")
print("=" * 50)
print(df.describe().round(1))

print("\n" + "=" * 50)
print("STEP 4: Categorical Distributions")
print("=" * 50)
print("City distribution:")
print(df["city"].value_counts())
print("\nDept distribution:")
print(df["dept"].value_counts())

print("\n" + "=" * 50)
print("STEP 5: Correlations")
print("=" * 50)
numeric_cols = ["age", "experience", "salary", "score"]
corr = df[numeric_cols].corr().round(2)
print(corr)

print("\n" + "=" * 50)
print("STEP 6: Group Analysis")
print("=" * 50)
print("Avg salary by dept:")
print(df.groupby("dept")["salary"].mean().round(0).sort_values(ascending=False))

print("\nAvg salary by city:")
print(df.groupby("city")["salary"].mean().round(0).sort_values(ascending=False))

print("\n" + "=" * 50)
print("STEP 7: Outlier Check (IQR)")
print("=" * 50)
for col in ["salary", "age", "experience"]:
    q1  = df[col].quantile(0.25)
    q3  = df[col].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)]
    print(f"  {col:12}: {len(outliers)} outliers")

print("\n" + "=" * 50)
print("EDA Complete! Data ready for modeling.")
print("=" * 50)
