class TeacherNotFoundException(Exception):
    """
    Exception raised when a teacher cannot be found in the system.
    """
    
    def __init__(self, teacher_identifier):
        """
        Initialize the exception with teacher identification information
        
        Args:
            teacher_identifier: Either teacher ID or email that wasn't found
        """
        self.teacher_identifier = teacher_identifier
        self.message = f"Teacher not found: {teacher_identifier}"
        super().__init__(self.message)

    def __str__(self):
        return self.message