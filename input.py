import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note (optional): ")

    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])

    print("Expense added!\n")

def init_file():
    try:
        with open(FILENAME, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "note"])
    except FileExistsError:
        pass

def main():
    init_file()
    while True:
        add_expense()
        cont = input("Add another? (y/n): ")
        if cont.lower() != "y":
            break

if __name__ == "__main__":
    main()
