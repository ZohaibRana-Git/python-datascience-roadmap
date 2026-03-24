# ============================================================
# Phase 2 | Topic 2: NumPy Operations
# ============================================================
# Math operations, broadcasting, statistics
# ============================================================

import numpy as np

np.random.seed(42)

# ─────────────────────────────────────────
# 1. Element-wise Operations
# ─────────────────────────────────────────
print("=== Element-wise Operations ===")
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(f"a + b  = {a + b}")
print(f"a * b  = {a * b}")
print(f"b / a  = {b / a}")
print(f"a ** 2 = {a ** 2}")
print(f"sqrt(b)= {np.sqrt(b)}")

# ─────────────────────────────────────────
# 2. Broadcasting
# ─────────────────────────────────────────
print("\n=== Broadcasting ===")
# Scalar ke saath operation — har element pe apply hota hai
arr = np.array([1, 2, 3, 4, 5])
print(f"arr * 10   = {arr * 10}")
print(f"arr + 100  = {arr + 100}")

# 2D broadcasting
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
row    = np.array([10, 20, 30])
print(f"\nmatrix + row:\n{matrix + row}")   # row har row me add hoti hai

# ─────────────────────────────────────────
# 3. Statistical Functions — Data Science core
# ─────────────────────────────────────────
print("\n=== Statistics ===")
data = np.array([23, 45, 12, 67, 34, 89, 56, 78, 43, 21])
print(f"Data   : {data}")
print(f"Mean   : {np.mean(data):.2f}")
print(f"Median : {np.median(data):.2f}")
print(f"Std    : {np.std(data):.2f}")
print(f"Var    : {np.var(data):.2f}")
print(f"Min    : {np.min(data)}")
print(f"Max    : {np.max(data)}")
print(f"Sum    : {np.sum(data)}")
print(f"25th % : {np.percentile(data, 25):.2f}")
print(f"75th % : {np.percentile(data, 75):.2f}")

# Axis-wise stats (2D)
m = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"\nMatrix:\n{m}")
print(f"Col means (axis=0): {np.mean(m, axis=0)}")   # per column
print(f"Row means (axis=1): {np.mean(m, axis=1)}")   # per row

# ─────────────────────────────────────────
# 4. Random Numbers — ML me bahut use
# ─────────────────────────────────────────
print("\n=== Random ===")
print(f"rand(3,3):\n{np.random.rand(3,3).round(2)}")          # 0-1 uniform
print(f"\nrandn(3,3):\n{np.random.randn(3,3).round(2)}")      # normal dist
print(f"\nrandint(1,100,10): {np.random.randint(1,100,10)}")  # integers

# ─────────────────────────────────────────
# 5. Linear Algebra — ML algorithms me use
# ─────────────────────────────────────────
print("\n=== Linear Algebra ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B (dot product):\n{A @ B}")
print(f"A.T (transpose):\n{A.T}")
print(f"det(A) = {np.linalg.det(A):.1f}")

# ─────────────────────────────────────────
# 6. Practical: Normalize scores
# ─────────────────────────────────────────
print("\n=== Practical: Normalization ===")
raw_scores = np.array([45, 82, 67, 91, 55, 78, 88, 43, 76, 60])

# Min-Max normalization
normalized = (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min())

# Z-score standardization
z_scores = (raw_scores - raw_scores.mean()) / raw_scores.std()

print(f"Raw       : {raw_scores}")
print(f"Normalized: {normalized.round(2)}")
print(f"Z-scores  : {z_scores.round(2)}")
