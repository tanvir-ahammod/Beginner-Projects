import csv

FILENAME = 'expenses.csv'

def add_expense(amount, category):
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses recorded.")
                return
            print("\nYour Expenses:")
            for amount, category in expenses:
                print(f"{category}: ${amount}")
    except FileNotFoundError:
        print("No expenses recorded.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            add_expense(amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()