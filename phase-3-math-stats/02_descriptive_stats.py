# ============================================================
# Phase 3 | Topic 2: Descriptive Statistics
# ============================================================
# Data ko summarize karna — pehla step har Data Science project me
# ============================================================

import numpy as np
import statistics

data = [23, 45, 12, 67, 34, 89, 56, 78, 43, 21, 56, 34, 67, 45, 89]
print(f"Data: {data}")
print(f"N   : {len(data)}")

# ─────────────────────────────────────────
# 1. Central Tendency
# ─────────────────────────────────────────
print("\n=== Central Tendency ===")
mean   = np.mean(data)
median = np.median(data)
mode   = statistics.mode(data)

print(f"Mean   : {mean:.2f}  ← average")
print(f"Median : {median:.2f}  ← middle value (outliers se safe)")
print(f"Mode   : {mode}    ← most frequent")

# Outlier ka effect
data_with_outlier = data + [1000]
print(f"\nWith outlier 1000:")
print(f"  Mean   : {np.mean(data_with_outlier):.2f}  ← bahut affect hua")
print(f"  Median : {np.median(data_with_outlier):.2f}  ← stable raha")

# ─────────────────────────────────────────
# 2. Spread / Variability
# ─────────────────────────────────────────
print("\n=== Spread ===")
arr = np.array(data)

variance = np.var(arr)
std_dev  = np.std(arr)
rng      = arr.max() - arr.min()
q1       = np.percentile(arr, 25)
q3       = np.percentile(arr, 75)
iqr      = q3 - q1

print(f"Variance : {variance:.2f}  ← average squared distance from mean")
print(f"Std Dev  : {std_dev:.2f}  ← sqrt(variance), same unit as data")
print(f"Range    : {rng}    ← max - min")
print(f"Q1       : {q1}")
print(f"Q3       : {q3}")
print(f"IQR      : {iqr}    ← Q3 - Q1, outlier-resistant spread")

# ─────────────────────────────────────────
# 3. Percentiles & Quartiles
# ─────────────────────────────────────────
print("\n=== Percentiles ===")
for p in [10, 25, 50, 75, 90, 95]:
    print(f"  {p:2}th percentile: {np.percentile(arr, p):.1f}")

# ─────────────────────────────────────────
# 4. Correlation
# ─────────────────────────────────────────
print("\n=== Correlation ===")
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
exam_scores = np.array([45, 52, 58, 65, 70, 75, 80, 85, 88, 92])
no_relation  = np.array([67, 23, 89, 45, 12, 78, 34, 56, 90, 11])

corr_positive = np.corrcoef(study_hours, exam_scores)[0,1]
corr_none     = np.corrcoef(study_hours, no_relation)[0,1]

print(f"Study hours vs Exam scores : r = {corr_positive:.3f}  (strong positive)")
print(f"Study hours vs Random data : r = {corr_none:.3f}  (no correlation)")
print("\nCorrelation guide:")
print("  r = +1.0  → perfect positive")
print("  r = +0.7  → strong positive")
print("  r =  0.0  → no correlation")
print("  r = -0.7  → strong negative")
print("  r = -1.0  → perfect negative")

# ─────────────────────────────────────────
# 5. Five Number Summary
# ─────────────────────────────────────────
print("\n=== Five Number Summary ===")
print(f"  Min    : {arr.min()}")
print(f"  Q1     : {q1}")
print(f"  Median : {np.median(arr)}")
print(f"  Q3     : {q3}")
print(f"  Max    : {arr.max()}")
