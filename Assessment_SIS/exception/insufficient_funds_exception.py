class InsufficientFundsException(Exception):
    """
    Exception raised when a student attempts to enroll in a course
    but doesn't have sufficient funds to make the required payment.
    """
    
    def __init__(self, student_id: int, required_amount: float, available_amount: float):
        """
        Initialize the exception with payment details
        
        Args:
            student_id: ID of the student with insufficient funds
            required_amount: Amount required for enrollment
            available_amount: Amount currently available
        """
        self.student_id = student_id
        self.required_amount = required_amount
        self.available_amount = available_amount
        self.message = (f"Student {student_id} has insufficient funds. "
                       f"Required: {required_amount:.2f}, Available: {available_amount:.2f}")
        super().__init__(self.message)

    def __str__(self):
        return self.message