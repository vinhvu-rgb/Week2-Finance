import os
import pandas as pd

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

    # Portfolio setup
    cash = 10000  # starting cash
    holdings = {}  # stock symbol -> shares held

    # Simulate trading per day per stock
    print("Trading Log:")
    print("------------")
    for index, row in df.iterrows():
        stock = row["Stock"]
        daily_return = row["Daily Return"]
        close_price = row["Close"]

        if stock not in holdings:
            holdings[stock] = 0

        # Simple strategy:
        # Buy 10 shares if daily return > 2%
        if daily_return > 0.02 and cash >= 10 * close_price:
            holdings[stock] += 10
            cash -= 10 * close_price
            print(f"{row['Date']} {stock}: Bought 10 shares at {close_price}")

        # Sell 5 shares if daily return < 1%
        elif daily_return < 0.01 and holdings[stock] >= 5:
            holdings[stock] -= 5
            cash += 5 * close_price
            print(f"{row['Date']} {stock}: Sold 5 shares at {close_price}")

    # Calculate final portfolio value
    portfolio_value = cash + sum(holdings[s] * df[df["Stock"] == s].iloc[-1]["Close"] for s in holdings)

    print("\nFinal Portfolio:")
    print(f"Cash: ${cash:.2f}")
    for stock, shares in holdings.items():
        print(f"{stock}: {shares} shares")
    print(f"Total Portfolio Value: ${portfolio_value:.2f}")

if __name__ == "__main__":
    main()
