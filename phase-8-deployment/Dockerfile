# ============================================================
# Dockerfile — ML API ko container me package karo
# ============================================================
# Build:  docker build -t salary-api .
# Run:    docker run -p 5000:5000 salary-api
# ============================================================

FROM python:3.11-slim

WORKDIR /app

# Dependencies pehle copy karo (caching ke liye)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App files copy karo
COPY . .

# Port expose karo
EXPOSE 5000

# App run karo
CMD ["python", "01_flask_api.py"]
