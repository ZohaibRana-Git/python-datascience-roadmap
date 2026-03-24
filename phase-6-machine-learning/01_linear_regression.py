# ============================================================
# Phase 6 | Topic 1: Linear Regression
# ============================================================
# Regression = continuous value predict karna
# Example: salary predict karna experience se
# y = mx + b  (line of best fit)
# pip install scikit-learn
# ============================================================

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# ─────────────────────────────────────────
# 1. Simple Linear Regression (1 feature)
# ─────────────────────────────────────────
print("=" * 50)
print("SIMPLE LINEAR REGRESSION")
print("=" * 50)

# Dataset: experience → salary
n = 200
experience = np.random.randint(0, 15, n)
salary     = experience * 15000 + 50000 + np.random.normal(0, 10000, n)

X = experience.reshape(-1, 1)   # 2D array chahiye sklearn ko
y = salary

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# Model train karo
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print(f"\nModel:")
print(f"  Coefficient (slope) : {model.coef_[0]:,.0f}")
print(f"  Intercept           : {model.intercept_:,.0f}")
print(f"  Formula: salary = {model.coef_[0]:,.0f} × experience + {model.intercept_:,.0f}")

print(f"\nMetrics:")
print(f"  RMSE : {rmse:,.0f}  (average error in PKR)")
print(f"  R²   : {r2:.4f}  (1.0 = perfect, 0 = useless)")

# Predictions
print(f"\nSample Predictions:")
for exp in [0, 3, 5, 10, 15]:
    pred = model.predict([[exp]])[0]
    print(f"  {exp} years experience → PKR {pred:,.0f}")

# ─────────────────────────────────────────
# 2. Multiple Linear Regression (multiple features)
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("MULTIPLE LINEAR REGRESSION")
print("=" * 50)

# Dataset: age, experience, score → salary
df = pd.DataFrame({
    "age"       : np.random.randint(22, 45, n),
    "experience": np.random.randint(0, 20, n),
    "score"     : np.random.randint(60, 100, n),
})
df["salary"] = (df["experience"] * 12000 +
                df["score"] * 500 +
                df["age"] * 1000 +
                np.random.normal(0, 8000, n))

X = df[["age", "experience", "score"]]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features (important for many algorithms)
scaler  = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

model_multi = LinearRegression()
model_multi.fit(X_train_scaled, y_train)
y_pred_multi = model_multi.predict(X_test_scaled)

r2_multi = r2_score(y_test, y_pred_multi)
rmse_multi = np.sqrt(mean_squared_error(y_test, y_pred_multi))

print(f"Features: {list(X.columns)}")
print(f"\nCoefficients:")
for feat, coef in zip(X.columns, model_multi.coef_):
    print(f"  {feat:12}: {coef:,.0f}")

print(f"\nMetrics:")
print(f"  RMSE : {rmse_multi:,.0f}")
print(f"  R²   : {r2_multi:.4f}")

# ─────────────────────────────────────────
# 3. Actual vs Predicted comparison
# ─────────────────────────────────────────
print(f"\nActual vs Predicted (first 8):")
print(f"  {'Actual':>12}  {'Predicted':>12}  {'Error':>10}")
print(f"  {'-'*38}")
for actual, pred in zip(y_test[:8], y_pred_multi[:8]):
    error = actual - pred
    print(f"  {actual:>12,.0f}  {pred:>12,.0f}  {error:>+10,.0f}")
