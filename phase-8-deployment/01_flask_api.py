# ============================================================
# Phase 8 | Topic 1: Flask ML API
# ============================================================
# ML model ko REST API me wrap karo
# pip install flask scikit-learn joblib numpy
# Run: python 01_flask_api.py
# Test: POST http://localhost:5000/predict
# ============================================================

import numpy as np
import joblib
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# ─────────────────────────────────────────
# Step 1: Model Train & Save
# ─────────────────────────────────────────
def train_and_save_model():
    """Ek simple model train karo aur save karo."""
    np.random.seed(42)
    n = 500

    experience = np.random.randint(0, 15, n)
    score      = np.random.randint(60, 100, n)
    salary     = experience * 12000 + score * 500 + 30000 + np.random.normal(0, 5000, n)

    X = np.column_stack([experience, score])
    y = salary

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    joblib.dump(model,  "salary_model.pkl")
    joblib.dump(scaler, "salary_scaler.pkl")
    print("Model saved: salary_model.pkl")
    return model, scaler

# Train model agar nahi hai
if not os.path.exists("salary_model.pkl"):
    train_and_save_model()

# ─────────────────────────────────────────
# Step 2: Flask API
# ─────────────────────────────────────────
try:
    from flask import Flask, request, jsonify

    app    = Flask(__name__)
    model  = joblib.load("salary_model.pkl")
    scaler = joblib.load("salary_scaler.pkl")

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Salary Prediction API",
            "version": "1.0",
            "endpoints": {
                "POST /predict": "Salary predict karo",
                "GET /health" : "API health check"
            }
        })

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok", "model": "LinearRegression"})

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            data = request.get_json()

            # Validate input
            if "experience" not in data or "score" not in data:
                return jsonify({"error": "experience aur score required hain"}), 400

            experience = float(data["experience"])
            score      = float(data["score"])

            # Validate ranges
            if not (0 <= experience <= 30):
                return jsonify({"error": "experience 0-30 ke beech hona chahiye"}), 400
            if not (0 <= score <= 100):
                return jsonify({"error": "score 0-100 ke beech hona chahiye"}), 400

            # Predict
            X = np.array([[experience, score]])
            X_scaled = scaler.transform(X)
            salary = model.predict(X_scaled)[0]

            return jsonify({
                "input": {
                    "experience": experience,
                    "score"     : score
                },
                "predicted_salary": round(salary, 0),
                "currency": "PKR"
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if __name__ == "__main__":
        print("Flask API starting...")
        print("URL: http://localhost:5000")
        print("Test: POST /predict  body: {experience: 5, score: 80}")
        app.run(debug=True, host="0.0.0.0", port=5000)

except ImportError:
    print("Flask install nahi hai. Run: pip install flask")
    print("\nAPI structure samajh lo:")
    print("  @app.route('/predict', methods=['POST'])")
    print("  def predict():")
    print("      data = request.get_json()")
    print("      X = scaler.transform([[data['experience'], data['score']]])")
    print("      salary = model.predict(X)[0]")
    print("      return jsonify({'salary': salary})")
