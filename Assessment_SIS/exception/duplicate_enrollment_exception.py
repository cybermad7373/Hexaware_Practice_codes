class DuplicateEnrollmentException(Exception):
    """
    Exception raised when a student is already enrolled in a course
    and attempts to enroll again.
    """
    
    def __init__(self, student_id: int, course_id: int):
        """
        Initialize the exception with student and course information
        
        Args:
            student_id: ID of the student attempting to enroll
            course_id: ID of the course being enrolled in
        """
        self.student_id = student_id
        self.course_id = course_id
        self.message = f"Student {student_id} is already enrolled in course {course_id}"
        super().__init__(self.message)

    def __str__(self):
        return self.message