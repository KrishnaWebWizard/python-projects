import csv
import datetime

# Function to add an expense to the CSV file
def add_expense(date, amount, category, description):
    with open('expenses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, amount, category, description])

# Function to list all expenses from the CSV file
def list_expenses():
    with open('expenses.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Function to calculate total spending
def total_spending():
    total = 0
    with open('expenses.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total += float(row[1])
    return total

# Function to calculate spending by category
def spending_by_category(category):
    total = 0
    with open('expenses.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2] == category:
                total += float(row[1])
    return total

# Function to filter expenses by date range
def filter_by_date(start_date, end_date):
    expenses = []
    with open('expenses.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expense_date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
            if start_date <= expense_date <= end_date:
                expenses.append(row)
    return expenses

# Main function
def main():
    # Example usage
    add_expense('2024-03-15', 50, 'Food', 'Lunch')
    add_expense('2024-03-15', 30, 'Transport', 'Taxi')
    add_expense('2024-03-16', 20, 'Food', 'Dinner')
    add_expense('2024-03-17', 100, 'Shopping', 'Clothes')

    print("List of all expenses:")
    list_expenses()

    print("\nTotal spending:", total_spending())

    print("\nSpending on food:", spending_by_category('Food'))

    start_date = datetime.datetime.strptime('2024-03-15', '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime('2024-03-16', '%Y-%m-%d').date()
    print("\nExpenses between", start_date, "and", end_date)
    print(filter_by_date(start_date, end_date))

if __name__ == "__main__":
    main()
