import datetime
from collections import defaultdict
import pyfiglet
import calendar
from prettytable import PrettyTable

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(list)
        self.categories = set()
        self.load_sample_data()  # Initialize with some sample data

    def load_sample_data(self):
        """Add some sample data for demonstration"""
        sample_expenses = [
            (1500.00, "Food", datetime.date(2023, 1, 15)),
            (2500.00, "Rent", datetime.date(2023, 1, 1)),
            (500.00, "Transport", datetime.date(2023, 1, 10)),
            (1200.00, "Food", datetime.date(2023, 2, 5)),
            (2500.00, "Rent", datetime.date(2023, 2, 1)),
            (800.00, "Entertainment", datetime.date(2023, 2, 20)),
        ]
        for amount, category, date in sample_expenses:
            self.add_expense(amount, category, date)

    def add_expense(self, amount, category, date=None):
        """Add a new expense with validation"""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            date = date or datetime.date.today()
            if not isinstance(date, datetime.date):
                raise ValueError("Invalid date format")
                
            category = category.strip().title()
            if not category:
                raise ValueError("Category cannot be empty")
                
            month_year = (date.month, date.year)
            self.expenses[month_year].append((amount, category, date))
            self.categories.add(category)
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def monthly_summary(self, month, year):
        """Get summary for a specific month"""
        key = (month, year)
        if key not in self.expenses:
            return 0
        return sum(exp[0] for exp in self.expenses[key])

    def yearly_summary(self, year):
        """Get summary for a specific year"""
        total = 0
        for month in range(1, 13):
            total += self.monthly_summary(month, year)
        return total

    def category_spending(self, month=None, year=None):
        """Get category-wise spending with optional month/year filter"""
        categories = defaultdict(float)
        
        if month and year:
            key = (month, year)
            month_data = self.expenses.get(key, [])
            for amount, category, _ in month_data:
                categories[category] += amount
        else:
            for month_data in self.expenses.values():
                for amount, category, _ in month_data:
                    categories[category] += amount
                    
        return dict(categories)

    def get_expense_history(self, limit=10):
        """Get recent expense history"""
        all_expenses = []
        for month_data in self.expenses.values():
            all_expenses.extend(month_data)
        
        # Sort by date descending
        all_expenses.sort(key=lambda x: x[2], reverse=True)
        return all_expenses[:limit]

    def _display_header(self, title):
        """Display consistent header with ASCII art"""
        print("\n" + "="*50)
        ascii_text = pyfiglet.figlet_format(title)
        print(ascii_text.center(50))
        print("="*50)

    def _display_expenses_table(self, expenses):
        """Display expenses in a formatted table"""
        if not expenses:
            print("No expenses found!")
            return
            
        table = PrettyTable()
        table.field_names = ["Date", "Category", "Amount"]
        table.align["Amount"] = "r"
        
        for amount, category, date in expenses:
            table.add_row([date.strftime("%Y-%m-%d"), category, f"₹{amount:.2f}"])
        
        print(table)

    def add_expense_interactive(self):
        """Interactive expense addition with validation"""
        while True:
            print("\nAdd New Expense (leave blank to cancel)")
            try:
                amount = input("Amount: ")
                if not amount:
                    return False
                    
                category = input("Category: ")
                if not category:
                    return False
                    
                date_str = input("Date (YYYY-MM-DD, leave blank for today): ")
                date = datetime.date.today()
                if date_str:
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                
                if self.add_expense(amount, category, date):
                    print("Expense added successfully!")
                    return True
                    
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

    def view_monthly_summary(self):
        """Interactive monthly summary view"""
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        
        total = self.monthly_summary(month, year)
        month_name = calendar.month_name[month]
        
        print(f"\nMonthly Summary for {month_name} {year}")
        print("-"*40)
        print(f"Total Expenses: ₹{total:.2f}")
        
        # Show category breakdown
        categories = self.category_spending(month, year)
        if categories:
            print("\nCategory-wise Breakdown:")
            for cat, amount in categories.items():
                print(f"{cat}: ₹{amount:.2f}")

    def run(self):
        while True:
            self._display_header("EXPENSE TRACKER")
            print("1. Add Expense")
            print("2. View Monthly Summary")
            print("3. View Yearly Summary")
            print("4. View Category Analysis")
            print("5. View Recent Expenses")
            print("6. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.add_expense_interactive()
            elif choice == '2':
                self.view_monthly_summary()
            elif choice == '3':
                year = int(input("Enter year: "))
                total = self.yearly_summary(year)
                print(f"\nYearly Summary for {year}")
                print("-"*40)
                print(f"Total Expenses: ₹{total:.2f}")
                
                # Monthly breakdown
                print("\nMonthly Breakdown:")
                for month in range(1, 13):
                    month_total = self.monthly_summary(month, year)
                    if month_total > 0:
                        print(f"{calendar.month_abbr[month]}: ₹{month_total:.2f}")
            elif choice == '4':
                print("\nCategory Analysis")
                print("1. Overall")
                print("2. For Specific Month")
                analysis_choice = input("Enter choice (1-2): ")
                
                if analysis_choice == '1':
                    categories = self.category_spending()
                    title = "Overall Category Spending"
                elif analysis_choice == '2':
                    year = int(input("Enter year: "))
                    month = int(input("Enter month (1-12): "))
                    categories = self.category_spending(month, year)
                    title = f"Category Spending for {calendar.month_name[month]} {year}"
                else:
                    print("Invalid choice!")
                    continue
                
                if categories:
                    print(f"\n{title}")
                    print("-"*40)
                    for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
                        print(f"{cat}: ₹{amount:.2f}")
                else:
                    print("No expenses found for the selected period!")
            elif choice == '5':
                print("\nRecent Expenses:")
                recent_expenses = self.get_expense_history()
                self._display_expenses_table(recent_expenses)
            elif choice == '6':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")