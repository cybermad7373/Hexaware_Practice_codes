class InvalidLoanException(Exception):
    def __init__(self, message="Invalid loan ID or loan does not exist"):
        self.message = message
        super().__init__(self.message)