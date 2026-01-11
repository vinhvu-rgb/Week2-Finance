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

    cash = 10000  # starting cash
    holdings = {}
    portfolio_history = []

    print("Trading Log:")
    print("------------")

    for index, row in df.iterrows():
        stock = row["Stock"]
        daily_return = row["Daily Return"]
        close_price = row["Close"]

        if stock not in holdings:
            holdings[stock] = 0

        # Buy if return > 2%
        if daily_return > 0.02 and cash >= 10 * close_price:
            holdings[stock] += 10
            cash -= 10 * close_price
            print(f"{row['Date']} {stock}: Bought 10 shares at {close_price}")

        # Sell if return < 1%
        elif daily_return < 0.01 and holdings[stock] >= 5:
            holdings[stock] -= 5
            cash += 5 * close_price
            print(f"{row['Date']} {stock}: Sold 5 shares at {close_price}")

        # Track portfolio value
        portfolio_value = cash + sum(holdings[s] * df[df["Stock"] == s].iloc[:index+1]["Close"].iloc[-1] for s in holdings)
        portfolio_history.append({
            "Date": row["Date"],
            "Portfolio Value": portfolio_value
        })

    # Final portfolio
    print("\nFinal Portfolio:")
    print(f"Cash: ${cash:.2f}")
    for stock, shares in holdings.items():
        print(f"{stock}: {shares} shares")
    print(f"Total Portfolio Value: ${portfolio_history[-1]['Portfolio Value']:.2f}")

    # Plot portfolio value over time
    portfolio_df = pd.DataFrame(portfolio_history)
    plt.plot(portfolio_df["Date"], portfolio_df["Portfolio Value"], marker='o')
    plt.title("Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
