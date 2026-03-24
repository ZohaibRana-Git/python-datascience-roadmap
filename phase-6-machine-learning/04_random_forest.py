# ============================================================
# Phase 6 | Topic 4: Random Forest
# ============================================================
# Random Forest = bahut saare Decision Trees ka ensemble
# Har tree alag data pe train hota hai → majority vote
# Akele Decision Tree se zyada accurate aur robust hota hai
# ============================================================

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
n = 500

# Dataset: Employee churn prediction
df = pd.DataFrame({
    "age"           : np.random.randint(22, 55, n),
    "experience"    : np.random.randint(0, 20, n),
    "salary"        : np.random.randint(50000, 300000, n),
    "satisfaction"  : np.random.randint(1, 10, n),
    "projects"      : np.random.randint(1, 8, n),
    "dept"          : np.random.choice(["DS","ML","Backend","Frontend"], n),
})

# Churn logic: low satisfaction ya low salary → likely to leave
churn_score = (10 - df["satisfaction"]) * 0.4 + (200000 - df["salary"]) / 50000 * 0.3
df["churned"] = (churn_score + np.random.normal(0, 0.5, n) > 2.5).astype(int)

print("=== Employee Churn Dataset ===")
print(df.head())
print(f"\nChurned: {df['churned'].sum()} | Stayed: {(df['churned']==0).sum()}")

# Encode categorical
le = LabelEncoder()
df["dept_enc"] = le.fit_transform(df["dept"])

features = ["age", "experience", "salary", "satisfaction", "projects", "dept_enc"]
X = df[features]
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ─────────────────────────────────────────
# Train Random Forest
# ─────────────────────────────────────────
rf = RandomForestClassifier(
    n_estimators=100,    # 100 trees
    max_depth=10,
    random_state=42,
    n_jobs=-1            # sab CPU cores use karo
)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Stayed","Churned"]))

# ─────────────────────────────────────────
# Feature Importance — Random Forest ka bonus
# ─────────────────────────────────────────
print("=== Feature Importance ===")
importances = pd.Series(rf.feature_importances_, index=features)
importances = importances.sort_values(ascending=False)
for feat, imp in importances.items():
    bar = "█" * int(imp * 50)
    print(f"  {feat:15}: {imp:.4f}  {bar}")

# ─────────────────────────────────────────
# Cross Validation — reliable evaluation
# ─────────────────────────────────────────
print("\n=== Cross Validation (5-fold) ===")
cv_scores = cross_val_score(rf, X, y, cv=5, scoring="accuracy")
print(f"CV Scores : {cv_scores.round(4)}")
print(f"Mean      : {cv_scores.mean():.4f}")
print(f"Std       : {cv_scores.std():.4f}")
