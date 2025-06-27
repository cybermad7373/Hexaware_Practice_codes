class Customer:
    def __init__(self, customer_id=None, name=None, email_address=None, phone_number=None, 
                 address=None, credit_score=None):
        self.__customer_id = customer_id
        self.__name = name
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__address = address
        self.__credit_score = credit_score

    # Getters
    def get_customer_id(self):
        return self.__customer_id
    
    def get_name(self):
        return self.__name
    
    def get_email_address(self):
        return self.__email_address
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    def get_credit_score(self):
        return self.__credit_score
    
    # Setters
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    
    def set_name(self, name):
        self.__name = name
    
    def set_email_address(self, email_address):
        self.__email_address = email_address
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_address(self, address):
        self.__address = address
    
    def set_credit_score(self, credit_score):
        self.__credit_score = credit_score
    
    def print_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__name}")
        print(f"Email Address: {self.__email_address}")
        print(f"Phone Number: {self.__phone_number}")
        print(f"Address: {self.__address}")
        print(f"Credit Score: {self.__credit_score}")