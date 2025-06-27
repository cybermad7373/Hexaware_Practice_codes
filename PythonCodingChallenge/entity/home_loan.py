from entity.loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, 
                 interest_rate=None, loan_term=None, loan_type="HomeLoan", 
                 loan_status="Pending", property_address=None, property_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, 
                         loan_term, loan_type, loan_status)
        self.__property_address = property_address
        self.__property_value = property_value

    # Getters
    def get_property_address(self):
        return self.__property_address
    
    def get_property_value(self):
        return self.__property_value
    
    # Setters
    def set_property_address(self, property_address):
        self.__property_address = property_address
    
    def set_property_value(self, property_value):
        self.__property_value = property_value
    
    def print_info(self):
        super().print_info()
        print(f"Property Address: {self.__property_address}")
        print(f"Property Value: {self.__property_value}")