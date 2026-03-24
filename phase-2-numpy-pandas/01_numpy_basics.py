# ============================================================
# Phase 2 | Topic 1: NumPy Basics
# ============================================================
# NumPy = Numerical Python
# Fast multi-dimensional arrays — Data Science ki backbone
# pip install numpy
# ============================================================

import numpy as np

print("NumPy version:", np.__version__)

# ─────────────────────────────────────────
# 1. Array Banao
# ─────────────────────────────────────────
print("\n=== Create Arrays ===")

a1 = np.array([1, 2, 3, 4, 5])                    # 1D
a2 = np.array([[1, 2, 3], [4, 5, 6]])              # 2D
a3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])       # 3D

print(f"1D: {a1}  shape={a1.shape}  ndim={a1.ndim}")
print(f"2D:\n{a2}  shape={a2.shape}  ndim={a2.ndim}")

# Special arrays
zeros  = np.zeros((3, 4))
ones   = np.ones((2, 3))
eye    = np.eye(3)              # identity matrix
rng    = np.arange(0, 20, 2)   # 0,2,4,...18
linsp  = np.linspace(0, 1, 5)  # 5 evenly spaced values 0→1

print(f"\nzeros(3,4):\n{zeros}")
print(f"\nones(2,3):\n{ones}")
print(f"\neye(3):\n{eye}")
print(f"\narange(0,20,2): {rng}")
print(f"linspace(0,1,5): {linsp}")

# ─────────────────────────────────────────
# 2. dtype — Data Type
# ─────────────────────────────────────────
print("\n=== dtype ===")
int_arr   = np.array([1, 2, 3], dtype=np.int32)
float_arr = np.array([1, 2, 3], dtype=np.float64)
bool_arr  = np.array([1, 0, 1, 0], dtype=bool)

print(f"int32  : {int_arr}   dtype={int_arr.dtype}")
print(f"float64: {float_arr}  dtype={float_arr.dtype}")
print(f"bool   : {bool_arr}  dtype={bool_arr.dtype}")

# Type conversion
converted = int_arr.astype(np.float64)
print(f"int→float: {converted}")

# ─────────────────────────────────────────
# 3. Indexing & Slicing
# ─────────────────────────────────────────
print("\n=== Indexing & Slicing ===")
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print(f"arr        : {arr}")
print(f"arr[2]     : {arr[2]}")
print(f"arr[-1]    : {arr[-1]}")
print(f"arr[1:4]   : {arr[1:4]}")
print(f"arr[::2]   : {arr[::2]}")    # every 2nd
print(f"arr[::-1]  : {arr[::-1]}")   # reverse

# 2D indexing
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"\nMatrix:\n{m}")
print(f"m[1,2]   = {m[1,2]}")        # row 1, col 2
print(f"m[0,:]   = {m[0,:]}")        # first row
print(f"m[:,1]   = {m[:,1]}")        # second column
print(f"m[1:,1:] =\n{m[1:,1:]}")    # sub-matrix

# ─────────────────────────────────────────
# 4. Boolean Indexing (Data Science me bahut use)
# ─────────────────────────────────────────
print("\n=== Boolean Indexing ===")
scores = np.array([45, 82, 67, 91, 55, 78, 88, 43])
print(f"Scores       : {scores}")
print(f"Pass (>=60)  : {scores[scores >= 60]}")
print(f"Fail (<60)   : {scores[scores < 60]}")
print(f"Between 70-90: {scores[(scores >= 70) & (scores <= 90)]}")

# ─────────────────────────────────────────
# 5. Reshape
# ─────────────────────────────────────────
print("\n=== Reshape ===")
flat = np.arange(1, 13)
print(f"flat (12,)  : {flat}")
print(f"reshape(3,4):\n{flat.reshape(3, 4)}")
print(f"reshape(2,6):\n{flat.reshape(2, 6)}")
print(f"flatten back: {flat.reshape(3,4).flatten()}")
