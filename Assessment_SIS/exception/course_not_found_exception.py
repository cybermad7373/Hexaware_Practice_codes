class CourseNotFoundException(Exception):
    """
    Exception raised when a course cannot be found in the system.
    """
    
    def __init__(self, course_identifier):
        """
        Initialize the exception with course identification information
        
        Args:
            course_identifier: Either course ID or course code that wasn't found
        """
        self.course_identifier = course_identifier
        self.message = f"Course not found: {course_identifier}"
        super().__init__(self.message)

    def __str__(self):
        return self.message