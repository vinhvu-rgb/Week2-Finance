import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Determine repo root
# -----------------------------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

data_folder = os.path.join(repo_root, "data")
images_folder = os.path.join(repo_root, "images")

os.makedirs(data_folder, exist_ok=True)
os.makedirs(images_folder, exist_ok=True)

# -----------------------------
# Portfolio Simulation
# -----------------------------
np.random.seed(42)
days = 100
initial_value = 10000
mean_daily_return = 0.001
volatility = 0.02

daily_returns = np.random.normal(loc=mean_daily_return, scale=volatility, size=days)

portfolio_values = [initial_value]
for r in daily_returns:
    portfolio_values.append(portfolio_values[-1] * (1 + r))

df = pd.DataFrame({
    "Day": range(days + 1),
    "Portfolio Value": portfolio_values
})

# -----------------------------
# Save CSV
# -----------------------------
csv_path = os.path.join(data_folder, "portfolio_values.csv")
df.to_csv(csv_path, index=False)

# -----------------------------
# Plot Portfolio
# -----------------------------
plt.figure(figsize=(10, 6))
plt.plot(df["Day"], df["Portfolio Value"], color="blue", lw=2)
plt.title("Portfolio Value Over Time")
plt.xlabel("Day")
plt.ylabel("Portfolio Value ($)")
plt.grid(True)
plt.tight_layout()

plot_path = os.path.join(images_folder, "portfolio_plot.png")
plt.savefig(plot_path, dpi=300)
plt.show()

print("Portfolio simulation complete.")
print(f"CSV saved to: {csv_path}")
print(f"Plot saved to: {plot_path}")

# Safety checks
if not os.path.exists(csv_path):
    print("Warning: CSV file was not saved correctly.")
if not os.path.exists(plot_path):
    print("Warning: Plot file was not saved correctly.")
