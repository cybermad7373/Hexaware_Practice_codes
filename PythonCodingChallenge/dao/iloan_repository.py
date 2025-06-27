from abc import ABC, abstractmethod
from entity.loan import Loan
from exception.invalid_loan_exception import InvalidLoanException

class ILoanRepository(ABC):
    @abstractmethod
    def apply_loan(self, loan):
        pass
    
    @abstractmethod
    def calculate_interest(self, loan_id):
        pass
    
    @abstractmethod
    def loan_status(self, loan_id):
        pass
    
    @abstractmethod
    def calculate_emi(self, loan_id):
        pass
    
    @abstractmethod
    def loan_repayment(self, loan_id, amount):
        pass
    
    @abstractmethod
    def get_all_loans(self):
        pass
    
    @abstractmethod
    def get_loan_by_id(self, loan_id):
        pass