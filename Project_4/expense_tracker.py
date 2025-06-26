import datetime
from collections import defaultdict
import pyfiglet

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(list)
        self.categories = set()

    def add_expense(self, amount, category, date=None):
        date = date or datetime.date.today()
        month_year = (date.month, date.year)
        self.expenses[month_year].append((amount, category, date))
        self.categories.add(category)

    def monthly_summary(self, month, year):
        key = (month, year)
        if key not in self.expenses:
            return 0
        return sum(exp[0] for exp in self.expenses[key])

    def yearly_summary(self, year):
        total = 0
        for month in range(1, 13):
            total += self.monthly_summary(month, year)
        return total

    def category_spending(self):
        categories = {}
        for month_data in self.expenses.values():
            for amount, category, _ in month_data:
                categories[category] = categories.get(category, 0) + amount
        return categories

    def run(self):
        while True:
            print("\n" + "="*50)
            ascii_text = pyfiglet.figlet_format("EXPENSE TRACKER")
            print(ascii_text.center(50))
            # print("EXPENSE TRACKER")
            print("="*50)
            print("1. Add Expense")
            print("2. View Monthly Summary")
            print("3. View Yearly Summary")
            print("4. View Category-wise Spending")
            print("5. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                amount = float(input("Enter amount spent: "))
                category = input("Enter category: ")
                self.add_expense(amount, category)
                print("Expense added successfully!")
            elif choice == '2':
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year: "))
                total = self.monthly_summary(month, year)
                print(f"Total expenses for {month}/{year}: ₹{total:.2f}")
            elif choice == '3':
                year = int(input("Enter year: "))
                total = self.yearly_summary(year)
                print(f"Total expenses for {year}: ₹{total:.2f}")
            elif choice == '4':
                print("\nCategory-wise Spending:")
                for cat, amount in self.category_spending().items():
                    print(f"{cat}: ₹{amount:.2f}")
            elif choice == '5':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")