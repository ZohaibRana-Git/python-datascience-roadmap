# Phase 8 — Deployment 🚀

> Model banane ke baad production me deploy karo — real users use kar sakein.

---

## Install

```bash
pip install flask fastapi uvicorn joblib scikit-learn
```

---

## Topics

| File              | Topic                                      |
|-------------------|--------------------------------------------|
| `01_flask_api.py` | Flask se ML model ko REST API banao        |
| `02_fastapi.py`   | FastAPI — modern, fast, auto docs          |
| `Dockerfile`      | Docker container me app package karo       |

---

## Deployment Flow

```
1. Model Train karo     → model.fit()
2. Model Save karo      → joblib.dump(model, 'model.pkl')
3. API banao            → Flask / FastAPI
4. Containerize         → Docker
5. Cloud pe deploy      → AWS / GCP / Heroku / Railway
```

---

## Run Flask API

```bash
python 01_flask_api.py
# API: http://localhost:5000/predict
```

## Run FastAPI

```bash
uvicorn 02_fastapi:app --reload
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## Test API (curl)

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"experience": 5, "score": 80}'
```

---

*Congratulations! Tum ne poora roadmap complete kar liya. 🎉*
