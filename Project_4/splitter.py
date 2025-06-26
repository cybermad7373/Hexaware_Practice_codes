import math
import pyfiglet
from collections import defaultdict

class BillSplitter:
    def __init__(self):
        self.participants = defaultdict(float)
    
    @staticmethod
    def _display_header():
        print("\n" + "="*50)
        ascii_text = pyfiglet.figlet_format("BILL SPLITTER")
        print(ascii_text.center(50))
        print("="*50)
    
    def _get_participants(self):
        self.participants.clear()
        print("\nEnter participant names (leave blank when done):")
        while True:
            name = input("Participant name: ").strip()
            if not name:
                if not self.participants:
                    print("Please add at least one participant!")
                    continue
                break
            self.participants[name] = 0.0
    
    def split_equal(self):
        total = float(input("Enter total bill amount: "))
        per_person = math.ceil((total / len(self.participants)) * 100) / 100
        for name in self.participants:
            self.participants[name] = per_person
        self._display_split(total)
    
    def split_by_percentage(self):
        total = float(input("Enter total bill amount: "))
        print("\nEnter percentage for each participant (must sum to 100%):")
        
        percentages = {}
        remaining = 100.0
        
        for name in list(self.participants.keys()):
            if len(self.participants) == 1:
                percent = 100.0
            else:
                max_percent = min(remaining, 100.0)
                prompt = f"Percentage for {name} (max {max_percent:.1f}%): "
                percent = float(input(prompt))
                while percent <= 0 or percent > max_percent:
                    print(f"Must be between 0 and {max_percent:.1f}")
                    percent = float(input(prompt))
            
            percentages[name] = percent
            remaining -= percent
        
        for name, percent in percentages.items():
            self.participants[name] = math.ceil(total * percent / 100 * 100) / 100
        
        # Adjust for rounding errors
        total_split = sum(self.participants.values())
        if total_split != total:
            first_person = next(iter(self.participants))
            self.participants[first_person] += total - total_split
        
        self._display_split(total)
    
    def split_by_weight(self):
        total = float(input("Enter total bill amount: "))
        print("\nEnter weight for each participant (higher weight pays more):")
        
        weights = {}
        total_weight = 0.0
        
        for name in self.participants:
            weight = float(input(f"Weight for {name}: "))
            while weight <= 0:
                print("Weight must be positive")
                weight = float(input(f"Weight for {name}: "))
            weights[name] = weight
            total_weight += weight
        
        for name, weight in weights.items():
            share = (weight / total_weight) * total
            self.participants[name] = math.ceil(share * 100) / 100
        
        # Adjust for rounding errors
        total_split = sum(self.participants.values())
        if total_split != total:
            first_person = next(iter(self.participants))
            self.participants[first_person] += total - total_split
        
        self._display_split(total)
    
    def split_with_tip(self):
        total = float(input("Enter total bill amount: "))
        tip_percent = float(input("Enter tip percentage: "))
        total_with_tip = total * (1 + tip_percent/100)
        
        print("\nChoose splitting method for the total (including tip):")
        print("1. Equal split")
        print("2. Percentage-based split")
        print("3. Weight-based split")
        
        method = input("Enter choice (1-3): ")
        {
            '1': self.split_equal,
            '2': self.split_by_percentage,
            '3': self.split_by_weight
        }[method](total_with_tip)
    
    def _display_split(self, total_amount):
        print("\n" + "="*50)
        print("BILL SPLIT RESULTS".center(50))
        print("="*50)
        print(f"Total Amount: ₹{total_amount:.2f}")
        print("-"*50)
        for name, amount in self.participants.items():
            print(f"{name}: ₹{amount:.2f}")
        print("="*50)
        print(f"Sum of splits: ₹{sum(self.participants.values()):.2f}")
        print("="*50)
    
    def run(self):
        while True:
            self._display_header()
            print("1. Equal Split")
            print("2. Percentage-based Split")
            print("3. Weight-based Split")
            print("4. Split with Tip")
            print("5. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self._get_participants()
                self.split_equal()
            elif choice == '2':
                self._get_participants()
                self.split_by_percentage()
            elif choice == '3':
                self._get_participants()
                self.split_by_weight()
            elif choice == '4':
                self._get_participants()
                self.split_with_tip()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")