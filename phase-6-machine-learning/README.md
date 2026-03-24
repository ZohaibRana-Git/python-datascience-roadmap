# Phase 6 — Machine Learning 🤖

> Yahan se real Data Science shuru hoti hai — algorithms se predictions karo.

---

## Install

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## Topics

| File                      | Algorithm                          | Type           |
|---------------------------|------------------------------------|----------------|
| `01_linear_regression.py` | Linear Regression                  | Regression     |
| `02_logistic_regression.py`| Logistic Regression               | Classification |
| `03_decision_tree.py`     | Decision Tree                      | Both           |
| `04_random_forest.py`     | Random Forest                      | Both           |
| `05_knn.py`               | K-Nearest Neighbors                | Both           |
| `06_clustering.py`        | K-Means Clustering                 | Unsupervised   |

---

## ML Workflow (Har project me same steps)

```
1. Data Load       → pd.read_csv()
2. EDA             → shape, nulls, describe
3. Preprocessing   → clean, encode, scale
4. Split           → train_test_split (80/20)
5. Train           → model.fit(X_train, y_train)
6. Predict         → model.predict(X_test)
7. Evaluate        → accuracy, MSE, R²
8. Improve         → tune hyperparameters
```

---

## Key Terms

| Term              | Meaning                                    |
|-------------------|--------------------------------------------|
| Features (X)      | Input variables (age, salary, etc.)        |
| Target (y)        | Output variable (price, pass/fail)         |
| Training set      | Model seekhta hai is data se (80%)         |
| Test set          | Model evaluate hota hai is data se (20%)  |
| Overfitting       | Training pe acha, test pe bura             |
| Underfitting      | Dono pe bura                               |

---

*Next: Phase 7 — Deep Learning 🧠*
