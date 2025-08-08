import csv
from datetime import datetime
import os

# Force the CSV file to be in the same directory as this script
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.csv")

def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    category = input("Enter category (e.g., Food, Transport): ").strip().title()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print(f"Added expense: {amount} in {category}.")

def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            expenses = list(reader)

            if not expenses:
                print("📂 No expenses recorded yet.")
                return

            print("\n--- All Expenses ---")
            for row in expenses:
                print(f"{row[0]} | {row[1]} | ${row[2]}")
    except FileNotFoundError:
        print("No expense file found.")

def view_total_per_category():
    totals = {}
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                category = row[1]
                amount = float(row[2])
                totals[category] = totals.get(category, 0) + amount

        if not totals:
            print("📂 No expenses recorded yet.")
            return

        print("\n--- Total Spend Per Category ---")
        for category, total in totals.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expense file found.")

def main():
    initialize_csv()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Per Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_per_category()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
