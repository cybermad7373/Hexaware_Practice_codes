class PaymentValidationException(Exception):
    """
    Exception raised when there is an issue with payment validation.
    """
    
    def __init__(self, message: str, payment_data: dict = None):
        """
        Initialize the exception with validation error details
        
        Args:
            message: Description of the validation error
            payment_data: Dictionary containing the payment data that failed validation
        """
        self.message = message
        self.payment_data = payment_data or {}
        super().__init__(self.message)

    def __str__(self):
        return f"Payment validation failed: {self.message}"