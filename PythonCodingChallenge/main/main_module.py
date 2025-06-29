import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.loan_repository_impl import LoanRepositoryImpl
from entity.customer import Customer
from entity.home_loan import HomeLoan
from entity.car_loan import CarLoan
from exception.invalid_loan_exception import InvalidLoanException

class MainModule:
    def __init__(self):
        self.loan_repo = LoanRepositoryImpl()
    
    def display_menu(self):
        print("\nLoan Management System")
        print("1. Apply for a Loan")
        print("2. Get All Loans")
        print("3. Get Loan by ID")
        print("4. Calculate Interest")
        print("5. Check Loan Status")
        print("6. Calculate EMI")
        print("7. Make Loan Repayment")
        print("8. Exit")
    
    def apply_loan(self):
        print("\nApply for a Loan")
        print("1. Home Loan")
        print("2. Car Loan")
        choice = input("Enter your choice: ")
        
        try:
            # Common loan details
            customer_id = int(input("Enter Customer ID: "))
            
            # Create a temporary customer object
            customer = Customer()
            customer.set_customer_id(customer_id)
            
            principal = float(input("Enter Principal Amount: "))
            interest_rate = float(input("Enter Interest Rate (annual %): "))
            term = int(input("Enter Loan Term (months): "))
            
            if choice == '1':
                # Home Loan specific details
                prop_address = input("Enter Property Address: ")
                prop_value = float(input("Enter Property Value: "))
                
                loan = HomeLoan(
                    customer=customer,
                    principal_amount=principal,
                    interest_rate=interest_rate,
                    loan_term=term,
                    property_address=prop_address,
                    property_value=prop_value
                )
            elif choice == '2':
                # Car Loan specific details
                car_model = input("Enter Car Model: ")
                car_value = float(input("Enter Car Value: "))
                
                loan = CarLoan(
                    customer=customer,
                    principal_amount=principal,
                    interest_rate=interest_rate,
                    loan_term=term,
                    car_model=car_model,
                    car_value=car_value
                )
            else:
                print("Invalid choice")
                return
            
            # Apply for loan
            if self.loan_repo.apply_loan(loan):
                print("Loan application submitted successfully!")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error applying for loan: {e}")
    
    def get_all_loans(self):
        print("\nAll Loans in the System")
        try:
            loans = self.loan_repo.get_all_loans()
            if loans:
                for loan in loans:
                    print("\nLoan ID:", loan['loan_id'])
                    print("Customer:", loan['customer_name'])
                    print("Type:", loan['loan_type'])
                    print("Principal:", loan['principal_amount'])
                    print("Status:", loan['loan_status'])
                    print("-----------------------")
        except Exception as e:
            print(f"Error retrieving loans: {e}")
    
    def get_loan_by_id(self):
        print("\nGet Loan Details by ID")
        try:
            loan_id = int(input("Enter Loan ID: "))
            loan = self.loan_repo.get_loan_by_id(loan_id)
            
            print("\nLoan Details:")
            print("ID:", loan['loan_id'])
            print("Customer:", loan['customer_name'])
            print("Type:", loan['loan_type'])
            print("Principal:", loan['principal_amount'])
            print("Interest Rate:", loan['interest_rate'])
            print("Term (months):", loan['loan_term'])
            print("Status:", loan['loan_status'])
            
            if loan['loan_type'] == 'HomeLoan':
                print("Property Address:", loan['property_address'])
                print("Property Value:", loan['property_value'])
            else:
                print("Car Model:", loan['car_model'])
                print("Car Value:", loan['car_value'])
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidLoanException:
            print("Loan not found with the given ID.")
        except Exception as e:
            print(f"Error retrieving loan: {e}")
    
    def calculate_interest(self):
        print("\nCalculate Interest for a Loan")
        try:
            loan_id = int(input("Enter Loan ID: "))
            interest = self.loan_repo.calculate_interest(loan_id)
            print(f"Interest amount: {interest:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidLoanException:
            print("Loan not found with the given ID.")
        except Exception as e:
            print(f"Error calculating interest: {e}")
    
    def check_loan_status(self):
        print("\nCheck Loan Status")
        try:
            loan_id = int(input("Enter Loan ID: "))
            status = self.loan_repo.loan_status(loan_id)
            print(f"Loan status: {status}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidLoanException:
            print("Loan not found with the given ID.")
        except Exception as e:
            print(f"Error checking loan status: {e}")
    
    def calculate_emi(self):      ## need to chek this later +++++++++++++++++++++++++++++++++++++++++++++++++++++ on dao implementaion file 
        print("\nCalculate EMI for a Loan")
        try:
            loan_id = int(input("Enter Loan ID: "))
            emi = self.loan_repo.calculate_emi(loan_id)
            print(f"Monthly EMI: {emi:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidLoanException:
            print("Loan not found with the given ID.")
        except Exception as e:
            print(f"Error calculating EMI: {e}")
    
    def make_repayment(self):
        print("\nMake Loan Repayment")
        try:
            loan_id = int(input("Enter Loan ID: "))
            amount = float(input("Enter Payment Amount: "))
            
            if self.loan_repo.loan_repayment(loan_id, amount):
                print("Payment processed successfully.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error processing payment: {e}")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.apply_loan()
            elif choice == '2':
                self.get_all_loans()
            elif choice == '3':
                self.get_loan_by_id()
            elif choice == '4':
                self.calculate_interest()
            elif choice == '5':
                self.check_loan_status()
            elif choice == '6':
                self.calculate_emi()
            elif choice == '7':
                self.make_repayment()
            elif choice == '8':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = MainModule()
    main.run()