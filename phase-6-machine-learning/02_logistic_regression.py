# ============================================================
# Phase 6 | Topic 2: Logistic Regression
# ============================================================
# Classification = category predict karna (pass/fail, spam/not spam)
# Logistic Regression → probability 0-1 → threshold → class
# ============================================================

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix)
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300

# Dataset: study_hours, attendance → pass/fail
study_hours = np.random.uniform(1, 10, n)
attendance  = np.random.uniform(50, 100, n)
noise       = np.random.normal(0, 0.5, n)

# Pass agar study_hours > 5 aur attendance > 70 (roughly)
score = study_hours * 0.6 + (attendance - 50) * 0.04 + noise
passed = (score > 4).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance" : attendance,
    "passed"     : passed
})

print("=== Dataset ===")
print(df.head())
print(f"\nPass: {passed.sum()} | Fail: {(passed==0).sum()}")

# ─────────────────────────────────────────
# Train / Test Split
# ─────────────────────────────────────────
X = df[["study_hours", "attendance"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# ─────────────────────────────────────────
# Train Model
# ─────────────────────────────────────────
model = LogisticRegression()
model.fit(X_train_s, y_train)

y_pred = model.predict(X_test_s)
y_prob = model.predict_proba(X_test_s)[:, 1]   # probability of passing

# ─────────────────────────────────────────
# Evaluate
# ─────────────────────────────────────────
print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Fail","Pass"]))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"  TN={cm[0,0]}  FP={cm[0,1]}")
print(f"  FN={cm[1,0]}  TP={cm[1,1]}")
print("\n  TN = Correctly predicted Fail")
print("  TP = Correctly predicted Pass")
print("  FP = Predicted Pass but actually Fail (Type I error)")
print("  FN = Predicted Fail but actually Pass (Type II error)")

# ─────────────────────────────────────────
# Predictions
# ─────────────────────────────────────────
print("\n=== Sample Predictions ===")
test_cases = [
    [2, 55],    # kam study, kam attendance → fail
    [8, 90],    # zyada study, zyada attendance → pass
    [5, 70],    # borderline
]

test_scaled = scaler.transform(test_cases)
preds = model.predict(test_scaled)
probs = model.predict_proba(test_scaled)[:, 1]

print(f"  {'Study Hrs':>10}  {'Attendance':>10}  {'Prediction':>12}  {'Probability':>12}")
print(f"  {'-'*50}")
for (sh, att), pred, prob in zip(test_cases, preds, probs):
    result = "PASS ✓" if pred == 1 else "FAIL ✗"
    print(f"  {sh:>10}  {att:>10}  {result:>12}  {prob:>11.1%}")
