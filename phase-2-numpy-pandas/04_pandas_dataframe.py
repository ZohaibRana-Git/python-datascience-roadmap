# ============================================================
# Phase 2 | Topic 4: Pandas — Filtering, GroupBy, Merge
# ============================================================

import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    "name"  : ["Ali","Sara","Ahmed","Zara","Bilal","Hina","Omar","Ayesha"],
    "age"   : [22, 20, 23, 21, 24, 22, 25, 21],
    "score" : [85, 92, 78, 95, 67, 88, 72, 91],
    "city"  : ["Karachi","Lahore","Islamabad","Karachi","Lahore","Islamabad","Karachi","Lahore"],
    "dept"  : ["DS","ML","DS","ML","DS","ML","DS","ML"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ─────────────────────────────────────────
# 1. Filtering
# ─────────────────────────────────────────
print("\n=== Filtering ===")
print("Score >= 85:")
print(df[df["score"] >= 85][["name","score"]])

print("\nCity == Karachi:")
print(df[df["city"] == "Karachi"][["name","city","score"]])

print("\nScore > 80 AND city == Lahore:")
mask = (df["score"] > 80) & (df["city"] == "Lahore")
print(df[mask][["name","score","city"]])

print("\nisin() — Karachi ya Lahore:")
print(df[df["city"].isin(["Karachi","Lahore"])][["name","city"]])

# ─────────────────────────────────────────
# 2. Sorting
# ─────────────────────────────────────────
print("\n=== Sorting ===")
print("By score (desc):")
print(df.sort_values("score", ascending=False)[["name","score"]].head(5))

print("\nBy city then score:")
print(df.sort_values(["city","score"], ascending=[True,False])[["name","city","score"]])

# ─────────────────────────────────────────
# 3. GroupBy — Data Science me bahut important
# ─────────────────────────────────────────
print("\n=== GroupBy ===")
city_stats = df.groupby("city")["score"].agg(["mean","max","min","count"])
city_stats.columns = ["avg_score","max_score","min_score","students"]
print("City-wise stats:")
print(city_stats.round(1))

dept_avg = df.groupby("dept")["score"].mean().round(1)
print(f"\nDept avg score:\n{dept_avg}")

# Multiple columns groupby
print("\nCity + Dept groupby:")
print(df.groupby(["city","dept"])["score"].mean().round(1))

# ─────────────────────────────────────────
# 4. Apply — custom function har row/col pe
# ─────────────────────────────────────────
print("\n=== Apply ===")

def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    else: return "D"

df["grade"] = df["score"].apply(grade)
print(df[["name","score","grade"]])

# ─────────────────────────────────────────
# 5. Merge / Join — SQL jaisa
# ─────────────────────────────────────────
print("\n=== Merge ===")
students = pd.DataFrame({
    "id"  : [1, 2, 3, 4],
    "name": ["Ali","Sara","Ahmed","Zara"]
})
scores = pd.DataFrame({
    "id"   : [1, 2, 3, 5],
    "score": [85, 92, 78, 88]
})

inner = pd.merge(students, scores, on="id", how="inner")
left  = pd.merge(students, scores, on="id", how="left")

print("Inner join:")
print(inner)
print("\nLeft join:")
print(left)

# ─────────────────────────────────────────
# 6. Pivot Table
# ─────────────────────────────────────────
print("\n=== Pivot Table ===")
pivot = df.pivot_table(values="score", index="city", columns="dept", aggfunc="mean")
print(pivot.round(1))
