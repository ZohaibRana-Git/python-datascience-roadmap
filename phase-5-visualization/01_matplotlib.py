# ============================================================
# Phase 5 | Topic 1: Matplotlib
# ============================================================
# pip install matplotlib
# Charts save honge — screen pe show nahi honge (server env)
# ============================================================

import matplotlib
matplotlib.use("Agg")   # GUI nahi — file me save karo
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

np.random.seed(42)

# ─────────────────────────────────────────
# 1. Line Chart — Time Series
# ─────────────────────────────────────────
months  = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
revenue = [120, 135, 148, 162, 175, 190, 185, 200, 215, 230, 245, 260]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, revenue, marker="o", color="steelblue", linewidth=2, markersize=6)
ax.fill_between(months, revenue, alpha=0.1, color="steelblue")
ax.set_title("Monthly Revenue 2025", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (thousands PKR)")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "01_line_chart.png"), dpi=100)
plt.close()
print("Saved: 01_line_chart.png")

# ─────────────────────────────────────────
# 2. Bar Chart — Category Comparison
# ─────────────────────────────────────────
depts  = ["Data Science", "ML", "Backend", "Frontend"]
avg_sal = [180000, 200000, 150000, 140000]
colors  = ["#2196F3", "#4CAF50", "#FF9800", "#9C27B0"]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(depts, avg_sal, color=colors, edgecolor="white", linewidth=0.5)
ax.bar_label(bars, fmt="{:,.0f}", padding=3, fontsize=9)
ax.set_title("Average Salary by Department", fontsize=14, fontweight="bold")
ax.set_ylabel("Salary (PKR)")
ax.set_ylim(0, 250000)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "02_bar_chart.png"), dpi=100)
plt.close()
print("Saved: 02_bar_chart.png")

# ─────────────────────────────────────────
# 3. Scatter Plot — Correlation
# ─────────────────────────────────────────
experience = np.random.randint(0, 15, 100)
salary     = experience * 12000 + np.random.randint(40000, 80000, 100)

fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(experience, salary, c=salary, cmap="viridis", alpha=0.7, s=60)
plt.colorbar(scatter, ax=ax, label="Salary")
ax.set_title("Experience vs Salary", fontsize=14, fontweight="bold")
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary (PKR)")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "03_scatter.png"), dpi=100)
plt.close()
print("Saved: 03_scatter.png")

# ─────────────────────────────────────────
# 4. Histogram — Distribution
# ─────────────────────────────────────────
scores = np.random.normal(75, 12, 500)   # mean=75, std=12

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(scores, bins=30, color="steelblue", edgecolor="white", alpha=0.8)
ax.axvline(scores.mean(), color="red",    linestyle="--", label=f"Mean: {scores.mean():.1f}")
ax.axvline(np.median(scores), color="green", linestyle="--", label=f"Median: {np.median(scores):.1f}")
ax.set_title("Score Distribution", fontsize=14, fontweight="bold")
ax.set_xlabel("Score")
ax.set_ylabel("Frequency")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "04_histogram.png"), dpi=100)
plt.close()
print("Saved: 04_histogram.png")

# ─────────────────────────────────────────
# 5. Subplots — Multiple charts ek figure me
# ─────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Data Science Dashboard", fontsize=16, fontweight="bold")

# Top-left: Line
axes[0,0].plot(months, revenue, "b-o", markersize=4)
axes[0,0].set_title("Revenue Trend")
axes[0,0].grid(True, alpha=0.3)

# Top-right: Bar
axes[0,1].bar(depts, avg_sal, color=colors)
axes[0,1].set_title("Salary by Dept")
axes[0,1].tick_params(axis="x", rotation=15)

# Bottom-left: Scatter
axes[1,0].scatter(experience, salary, alpha=0.5, s=20, c="steelblue")
axes[1,0].set_title("Experience vs Salary")

# Bottom-right: Histogram
axes[1,1].hist(scores, bins=25, color="green", alpha=0.7)
axes[1,1].set_title("Score Distribution")

plt.tight_layout()
plt.savefig(os.path.join(OUT, "05_dashboard.png"), dpi=100)
plt.close()
print("Saved: 05_dashboard.png")

print(f"\nAll charts saved in: {OUT}")
