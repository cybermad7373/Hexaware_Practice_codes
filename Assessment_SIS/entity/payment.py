from datetime import date
from typing import Optional

class Payment:
    """Represents a payment made by a student"""
    
    def __init__(self, payment_id: Optional[int] = None,
                 student_id: Optional[int] = None,
                 amount: Optional[float] = None,
                 payment_date: Optional[str] = None):
        """
        Initialize a Payment object with provided attributes
        
        Args:
            payment_id: Unique identifier for the payment
            student_id: ID of the student who made the payment
            amount: Payment amount
            payment_date: Date of payment (YYYY-MM-DD)
        """
        self._payment_id = payment_id
        self._student_id = student_id
        self._amount = amount
        self._payment_date = payment_date

    # Property for payment_id
    @property
    def payment_id(self) -> Optional[int]:
        return self._payment_id
    
    @payment_id.setter
    def payment_id(self, value: int):
        if value <= 0:
            raise ValueError("Payment ID must be positive")
        self._payment_id = value

    # Property for student_id
    @property
    def student_id(self) -> Optional[int]:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value: int):
        if value <= 0:
            raise ValueError("Student ID must be positive")
        self._student_id = value

    # Property for amount
    @property
    def amount(self) -> Optional[float]:
        return self._amount
    
    @amount.setter
    def amount(self, value: float):
        if value <= 0:
            raise ValueError("Payment amount must be positive")
        self._amount = round(value, 2)

    # Property for payment_date
    @property
    def payment_date(self) -> Optional[str]:
        return self._payment_date
    
    @payment_date.setter
    def payment_date(self, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError("Payment date must be in YYYY-MM-DD format")
        self._payment_date = value

    def __str__(self) -> str:
        return f"Payment(ID: {self.payment_id}, Student: {self.student_id}, Amount: {self.amount})"

    def to_dict(self) -> dict:
        """Convert Payment object to dictionary"""
        return {
            'payment_id': self.payment_id,
            'student_id': self.student_id,
            'amount': self.amount,
            'payment_date': self.payment_date
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Payment':
        """Create Payment object from dictionary"""
        return cls(
            payment_id=data.get('payment_id'),
            student_id=data.get('student_id'),
            amount=data.get('amount'),
            payment_date=data.get('payment_date')
        )