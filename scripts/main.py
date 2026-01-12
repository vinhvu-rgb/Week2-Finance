import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Ensure folders exist
# -----------------------------
os.makedirs("../images", exist_ok=True)  # Save images in the images/ folder

# -----------------------------
# Portfolio Simulation
# -----------------------------

# Simulation parameters
np.random.seed(42)        # For reproducibility
days = 100                # Number of days
initial_value = 10000     # Starting portfolio value
mean_daily_return = 0.001 # Average daily return
volatility = 0.02         # Daily return volatility

# Generate daily returns using normal distribution
daily_returns = np.random.normal(loc=mean_daily_return, scale=volatility, size=days)

# Calculate portfolio value over time
portfolio_values = [initial_value]
for r in daily_returns:
    portfolio_values.append(portfolio_values[-1] * (1 + r))

# Create a DataFrame
df = pd.DataFrame({
    "Day": range(days + 1),
    "Portfolio Value": portfolio_values
})

# -----------------------------
# Save portfolio data (optional)
# -----------------------------
os.makedirs("../data", exist_ok=True)
df.to_csv("../data/portfolio_values.csv", index=False)

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

# Save the plot
plt.savefig("../images/portfolio_plot.png", dpi=300)
plt.show()

print("Portfolio simulation complete. Plot saved in images/portfolio_plot.png")
