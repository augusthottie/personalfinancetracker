# a program to track user finances
import json

#initialize variables 
income = 0.0
expenses = []
savings = 0.0

#Load transactions data from file
def load_data():
    global income, expenses, savings
    try:
        with open('transactions.json', 'r') as file:
            data = json.load(file)
            income = data.get('income', 0.0)
            expenses = data.get('expenses', [])
            savings = data.get('savings', 0.0)
    except FileNotFoundError:
        pass

#Save transactions data to file
def save_data():
    global income, expenses, savings
    data = {
        'income': income,
        'expenses': expenses,
        'savings': savings
    }
    with open('transactions.json', 'w') as file:
        json.dump(data, file)

#Add a transaction for income
def add_income():
    global income
    amount = float(input('Enter income amount: '))
    income += amount
    print(f'Income of {amount} added successfully!')

#Add a transaction for expense
def add_expense():
    global expenses
    description = input('Enter expense description: ')
    amount = float(input('Enter expense amount: '))
    category = input('Enter expense category: ')
    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)
    print('Expense added successfully!')

#calculate savings
def calculate_savings():
    global income, expenses, savings
    savings = income - sum(expenses['amount'] for expenses in expenses)
    print(f'You have {savings} savings.')

#generate report of expenses by category
def generate_expense_report_category():
    category = input('Enter category: ')
    total_amount = sum(expense['amount'] for expense in expenses if expense['category'] == category)
    print(f'You have spent {total_amount} on {category}')

#run program
def main():
    load_data()

    while True:
        print('''==========Welcome to the Personal Finance Tracker!!============''')
        print("1. Add income")
        print("2. Add expense")
        print("3. Calculate savings")
        print("4. Generate expense report by category")
        print("5. Exit")

        choice = int(input('Enter your choice(1-5): '))
        if choice == 1 :
            add_income()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            calculate_savings()
        elif choice == 4:
            generate_expense_report_category()
        elif choice == 5:
            save_data()
            print("Thank you for using the tracker!")
            break
        else:
            print('Invalid choice! Try again with a valid choice.')

if __name__ == '__main__':
    main()
        