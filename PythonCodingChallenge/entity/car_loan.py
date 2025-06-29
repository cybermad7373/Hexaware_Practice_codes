from entity.loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, 
                 interest_rate=None, loan_term=None, loan_type="CarLoan", 
                 loan_status="Pending", car_model=None, car_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, 
                         loan_term, loan_type, loan_status)
        self.__car_model = car_model
        self.__car_value = car_value

    def get_car_model(self):
        return self.__car_model
    
    def get_car_value(self):
        return self.__car_value
    
    def set_car_model(self, car_model):
        self.__car_model = car_model
    
    def set_car_value(self, car_value):
        self.__car_value = car_value
    
    def print_info(self):
        super().print_info()
        print(f"Car Model: {self.__car_model}")
        print(f"Car Value: {self.__car_value}")