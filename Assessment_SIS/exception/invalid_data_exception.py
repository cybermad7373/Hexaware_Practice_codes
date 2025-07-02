class InvalidStudentDataException(Exception):
    """
    Exception raised when invalid student data is provided.
    """
    
    def __init__(self, field_name: str, field_value: str, reason: str):
        """
        Initialize the exception with field-specific error information
        
        Args:
            field_name: Name of the field with invalid data
            field_value: The invalid value that was provided
            reason: Explanation of why the value is invalid
        """
        self.field_name = field_name
        self.field_value = field_value
        self.reason = reason
        self.message = f"Invalid student data: {field_name}='{field_value}' - {reason}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidCourseDataException(Exception):
    """
    Exception raised when invalid course data is provided.
    """
    
    def __init__(self, field_name: str, field_value: str, reason: str):
        """
        Initialize the exception with field-specific error information
        
        Args:
            field_name: Name of the field with invalid data
            field_value: The invalid value that was provided
            reason: Explanation of why the value is invalid
        """
        self.field_name = field_name
        self.field_value = field_value
        self.reason = reason
        self.message = f"Invalid course data: {field_name}='{field_value}' - {reason}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidEnrollmentDataException(Exception):
    """
    Exception raised when invalid enrollment data is provided.
    """
    
    def __init__(self, field_name: str, field_value: str, reason: str):
        """
        Initialize the exception with field-specific error information
        
        Args:
            field_name: Name of the field with invalid data
            field_value: The invalid value that was provided
            reason: Explanation of why the value is invalid
        """
        self.field_name = field_name
        self.field_value = field_value
        self.reason = reason
        self.message = f"Invalid enrollment data: {field_name}='{field_value}' - {reason}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidTeacherDataException(Exception):
    """
    Exception raised when invalid teacher data is provided.
    """
    
    def __init__(self, field_name: str, field_value: str, reason: str):
        """
        Initialize the exception with field-specific error information
        
        Args:
            field_name: Name of the field with invalid data
            field_value: The invalid value that was provided
            reason: Explanation of why the value is invalid
        """
        self.field_name = field_name
        self.field_value = field_value
        self.reason = reason
        self.message = f"Invalid teacher data: {field_name}='{field_value}' - {reason}"
        super().__init__(self.message)

    def __str__(self):
        return self.message