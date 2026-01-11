import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "multi_stock.csv")

    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    df = pd.read_csv(file_path)
    df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Open", "Close"])

    # Calculate daily return
    df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"]

    # Summary stats per stock
    for stock, group in df.groupby("Stock"):
        avg_return = group["Daily Return"].mean()
        best_day = group.loc[group["Daily Return"].idxmax()]
        worst_day = group.loc[group["Daily Return"].idxmin()]
        print(f"\n{stock} Summary:")
        print(f"Average Return: {avg_return:.2%}")
        print(f"Best Day: {best_day['Date']} ({best_day['Daily Return']:.2%})")
        print(f"Worst Day: {worst_day['Date']} ({worst_day['Daily Return']:.2%})")

        # Plot Close price
        plt.plot(group["Date"], group["Close"], label=stock)

    plt.title("Stock Close Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
