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
        df = df.dropna(subset=["Open", "Close"])

        # Calculate daily return
        df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"]

        # Summary statistics
        average_return = df["Daily Return"].mean()
        best_day = df.loc[df["Daily Return"].idxmax()]
        worst_day = df.loc[df["Daily Return"].idxmin()]

        print("Summary Statistics (pandas)")
        print("---------------------------")
        print(f"Average Daily Return: {average_return:.2%}")
        print(f"Best Day: {best_day['Date']} ({best_day['Daily Return']:.2%})")
        print(f"Worst Day: {worst_day['Date']} ({worst_day['Daily Return']:.2%})\n")

        # --- Mini trading strategy ---
        print("Mini Trading Strategy")
        print("--------------------")

        cash = 1000  # starting cash
        position = 0  # number of shares held

        for index, row in df.iterrows():
            # If daily return > 2%, buy 10 shares
            if row["Daily Return"] > 0.02:
                position += 10
                cash -= 10 * row["Close"]
                print(f"{row['Date']}: Bought 10 shares at {row['Close']}")
            # If daily return < 1%, sell 5 shares
            elif row["Daily Return"] < 0.01 and position >= 5:
                position -= 5
                cash += 5 * row["Close"]
                print(f"{row['Date']}: Sold 5 shares at {row['Close']}")

        # Final portfolio value
        final_value = cash + position * df.iloc[-1]["Close"]
        print(f"\nFinal cash: ${cash:.2f}")
        print(f"Shares held: {position}")
        print(f"Portfolio value: ${final_value:.2f}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
