from dao.iloan_repository import ILoanRepository
from entity.customer import Customer
from entity.loan import Loan
from entity.home_loan import HomeLoan
from entity.car_loan import CarLoan
from exception.invalid_loan_exception import InvalidLoanException
from util.db_conn_util import DBConnUtil
import mysql.connector

class LoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()
    
    def __del__(self):
        try:
            if hasattr(self, 'connection') and self.connection.is_connected():
                self.connection.close()
        except:
            pass
    
    def apply_loan(self, loan):
        try:
            cursor = self.connection.cursor()
            
            # Get customer details from the loan object
            customer = loan.get_customer()
            
            # Check if customer exists
            cursor.execute("SELECT * FROM Customer WHERE customer_id = %s", (customer.get_customer_id(),))
            customer_data = cursor.fetchone()
            
            if not customer_data:
                print("Customer does not exist. Please register the customer first.")
                return False
            
            # Get confirmation from user
            confirmation = input("Confirm loan application (yes/no): ").lower()
            if confirmation != 'yes':
                print("Loan application cancelled.")
                return False
            
            # Insert loan into database based on loan type
            if isinstance(loan, HomeLoan):
                query = """
                INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term, 
                                loan_type, loan_status, property_address, property_value)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    customer.get_customer_id(),
                    loan.get_principal_amount(),
                    loan.get_interest_rate(),
                    loan.get_loan_term(),
                    'HomeLoan',
                    'Pending',
                    loan.get_property_address(),
                    loan.get_property_value()
                )
            elif isinstance(loan, CarLoan):
                query = """
                INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term, 
                                loan_type, loan_status, car_model, car_value)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    customer.get_customer_id(),
                    loan.get_principal_amount(),
                    loan.get_interest_rate(),
                    loan.get_loan_term(),
                    'CarLoan',
                    'Pending',
                    loan.get_car_model(),
                    loan.get_car_value()
                )
            else:
                print("Invalid loan type")
                return False
            
            cursor.execute(query, values)
            self.connection.commit()
            print("Loan application submitted successfully!")
            return True
        except mysql.connector.Error as err:
            print(f"Error applying for loan: {err}")
            return False
    
    def calculate_interest(self, loan_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get loan details from database
            cursor.execute("SELECT * FROM Loan WHERE loan_id = %s", (loan_id,))
            loan_data = cursor.fetchone()
            
            if not loan_data:
                raise InvalidLoanException()
            
            # Calculate interest
            principal = loan_data['principal_amount']
            rate = loan_data['interest_rate']
            term = loan_data['loan_term']
            
            interest = (principal * rate * term) / (12 * 100)
            return interest
        except mysql.connector.Error as err:
            print(f"Error calculating interest: {err}")
            raise
    
    def loan_status(self, loan_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get loan and customer details
            cursor.execute("""
                SELECT l.*, c.credit_score 
                FROM Loan l
                JOIN Customer c ON l.customer_id = c.customer_id
                WHERE l.loan_id = %s
            """, (loan_id,))
            loan_data = cursor.fetchone()
            
            if not loan_data:
                raise InvalidLoanException()
            
            # Determine loan status based on credit score
            new_status = 'Approved' if loan_data['credit_score'] > 650 else 'Rejected'
            
            # Update loan status in database
            update_query = "UPDATE Loan SET loan_status = %s WHERE loan_id = %s"
            cursor.execute(update_query, (new_status, loan_id))
            self.connection.commit()
            
            print(f"Loan status updated to: {new_status}")
            return new_status
        except mysql.connector.Error as err:
            print(f"Error updating loan status: {err}")
            raise
    
    def calculate_emi(self, loan_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get loan details from database
            cursor.execute("SELECT * FROM Loan WHERE loan_id = %s", (loan_id,))
            loan_data = cursor.fetchone()
            
            if not loan_data:
                raise InvalidLoanException()
            
            # Calculate EMI
            principal = loan_data['principal_amount']
            annual_rate = loan_data['interest_rate']
            term = loan_data['loan_term']
            
            monthly_rate = annual_rate / (12 * 100)
            emi = (principal * monthly_rate * (1 + monthly_rate)**term) / ((1 + monthly_rate)**term - 1)
            
            return emi
        except mysql.connector.Error as err:
            print(f"Error calculating EMI: {err}")
            raise
    
    def loan_repayment(self, loan_id, amount):
        try:
            emi = self.calculate_emi(loan_id)
            
            if amount < emi:
                print("Payment rejected. Amount is less than one EMI.")
                return False
            
            no_of_emis = amount // emi
            remaining_amount = amount - (no_of_emis * emi)
            
            print(f"Payment accepted. {no_of_emis} EMIs paid.")
            if remaining_amount > 0:
                print(f"Remaining amount: {remaining_amount:.2f} will not be applied to loan.")
            
            return True
        except Exception as e:
            print(f"Error processing repayment: {e}")
            return False
    
    def get_all_loans(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get all loans with customer details
            cursor.execute("""
                SELECT l.*, c.name as customer_name, c.email_address, c.phone_number
                FROM Loan l
                JOIN Customer c ON l.customer_id = c.customer_id
            """)
            
            loans = cursor.fetchall()
            
            if not loans:
                print("No loans found in the system.")
                return []
            
            return loans
        except mysql.connector.Error as err:
            print(f"Error retrieving loans: {err}")
            return []
    
    def get_loan_by_id(self, loan_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get loan with customer details
            cursor.execute("""
                SELECT l.*, c.name as customer_name, c.email_address, c.phone_number
                FROM Loan l
                JOIN Customer c ON l.customer_id = c.customer_id
                WHERE l.loan_id = %s
            """, (loan_id,))
            
            loan_data = cursor.fetchone()
            
            if not loan_data:
                raise InvalidLoanException()
            
            return loan_data
        except mysql.connector.Error as err:
            print(f"Error retrieving loan: {err}")
            raise