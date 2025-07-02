class StudentNotFoundException(Exception):
    """
    Exception raised when a student cannot be found in the system.
    """
    
    def __init__(self, student_identifier):
        """
        Initialize the exception with student identification information
        
        Args:
            student_identifier: Either student ID or email that wasn't found
        """
        self.student_identifier = student_identifier
        self.message = f"Student not found: {student_identifier}"
        super().__init__(self.message)

    def __str__(self):
        return self.message