import csv
import os

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "sample_stock.csv")

    print("Daily Returns:")

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            open_price = float(row["Open"])
            close_price = float(row["Close"])

            daily_return = (close_price - open_price) / open_price

            print(f"{row['Date']}: {daily_return:.2%}")

if __name__ == "__main__":
    main()
