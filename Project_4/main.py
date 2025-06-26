import os
from expense_tracker import ExpenseTracker
from report_card import ReportCardSystem
from quiz import QuizApp
from splitter import BillSplitter
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    ascii_text = pyfiglet.figlet_format("Welcome   : )")
    print(ascii_text)
    print("MAIN MENU".center(50))
    print("="*50)
    print("1. Expense Tracker")
    print("2. Student Report Card System")
    print("3. Quiz Application")
    print("4. Bill Splitter")
    print("5. Exit")
    print("="*50)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            ExpenseTracker().run()
        elif choice == '2':
            ReportCardSystem().run()
        elif choice == '3':
            QuizApp().run()
        elif choice == '4':
            BillSplitter().run()
        elif choice == '5':
            print("Thank you for using the application!")
            break
        else:
            input("Invalid choice! Press Enter to continue...")

if __name__ == "__main__":
    main()