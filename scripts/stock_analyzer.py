import os
import pandas as pd

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "sample_stock.csv")

    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    try:
        df = pd.read_csv(file_path)

        # Convert Open and Close to numeric
        df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

        # Drop rows with missing or invalid data
        df = df.dropna(subset=["Open", "Close"])

        # Calculate daily return
        df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"]

        # Summary stats
        average_return = df["Daily Return"].mean()
        best_day = df.loc[df["Daily Return"].idxmax()]
        worst_day = df.loc[df["Daily Return"].idxmin()]

        print("Summary Statistics (pandas)")
        print("---------------------------")
        print(f"Average Daily Return: {average_return:.2%}")
        print(f"Best Day: {best_day['Date']} ({best_day['Daily Return']:.2%})")
        print(f"Worst Day: {worst_day['Date']} ({worst_day['Daily Return']:.2%})")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
