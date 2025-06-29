from entity.customer import Customer

class Loan:
    def __init__(self, loan_id=None, customer=None, principal_amount=None, 
                 interest_rate=None, loan_term=None, loan_type=None, loan_status="Pending"):
        self.__loan_id = loan_id
        self.__customer = customer
        self.__principal_amount = principal_amount
        self.__interest_rate = interest_rate
        self.__loan_term = loan_term
        self.__loan_type = loan_type
        self.__loan_status = loan_status

    # Gett
    def get_loan_id(self):
        return self.__loan_id
    
    def get_customer(self):
        return self.__customer
    
    def get_principal_amount(self):
        return self.__principal_amount
    
    def get_interest_rate(self):
        return self.__interest_rate
    
    def get_loan_term(self):
        return self.__loan_term
    
    def get_loan_type(self):
        return self.__loan_type
    
    def get_loan_status(self):
        return self.__loan_status
    
    # Sett
    def set_loan_id(self, loan_id):
        self.__loan_id = loan_id
    
    def set_customer(self, customer):
        self.__customer = customer
    
    def set_principal_amount(self, principal_amount):
        self.__principal_amount = principal_amount
    
    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate
    
    def set_loan_term(self, loan_term):
        self.__loan_term = loan_term
    
    def set_loan_type(self, loan_type):
        self.__loan_type = loan_type
    
    def set_loan_status(self, loan_status):
        self.__loan_status = loan_status
    
    def print_info(self):
        print(f"Loan ID: {self.__loan_id}")
        print(f"Customer ID: {self.__customer.get_customer_id()}")
        print(f"Principal Amount: {self.__principal_amount}")
        print(f"Interest Rate: {self.__interest_rate}")
        print(f"Loan Term (months): {self.__loan_term}")
        print(f"Loan Type: {self.__loan_type}")
        print(f"Loan Status: {self.__loan_status}")