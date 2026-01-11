import csv
import os

def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "sample_stock.csv")

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        print("Stock Data:")
        for row in reader:
            print(row)

if __name__ == "__main__":
    main()

