import csv
import os

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "sample_stock.csv")

    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    returns = []

    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    open_price = float(row["Open"])
                    close_price = float(row["Close"])
                except ValueError:
                    print(f"Skipping invalid row: {row}")
                    continue

                daily_return = (close_price - open_price) / open_price
                returns.append({
                    "date": row["Date"],
                    "return": daily_return
                })

    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    if not returns:
        print("No valid data to analyze.")
        return

    average_return = sum(r["return"] for r in returns) / len(returns)
    best_day = max(returns, key=lambda x: x["return"])
    worst_day = min(returns, key=lambda x: x["return"])

    print("Summary Statistics")
    print("------------------")
    print(f"Average Daily Return: {average_return:.2%}")
    print(f"Best Day: {best_day['date']} ({best_day['return']:.2%})")
    print(f"Worst Day: {worst_day['date']} ({worst_day['return']:.2%})")

if __name__ == "__main__":
    main()
