import math
import pyfiglet

class BillSplitter:
    @staticmethod
    def split_bill(total, people, tip_percent=0):
        total_with_tip = total * (1 + tip_percent/100)
        per_person = total_with_tip / people
        return math.ceil(per_person * 100) / 100  # Round up to 2 decimal places

    def run(self):
        while True:
            print("\n" + "="*50)
            ascii_text = pyfiglet.figlet_format("BILL SPLITTER")
            print(ascii_text.center(50))            
            # print("BILL SPLITTER".center(50))
            print("="*50)
            print("1. Split Bill Equally")
            print("2. Split Bill with Tip")
            print("3. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                total = float(input("Enter total bill amount: "))
                people = int(input("Enter number of people: "))
                amount = self.split_bill(total, people)
                print(f"\nEach person should pay: ₹{amount:.2f}")
            elif choice == '2':
                total = float(input("Enter total bill amount: "))
                people = int(input("Enter number of people: "))
                tip = float(input("Enter tip percentage: "))
                amount = self.split_bill(total, people, tip)
                print(f"\nEach person should pay: ₹{amount:.2f} (including {tip}% tip)")
            elif choice == '3':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")