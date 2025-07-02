from datetime import date
from typing import Optional

class Enrollment:
    """Represents a student's enrollment in a course"""
    
    def __init__(self, enrollment_id: Optional[int] = None,
                 student_id: Optional[int] = None,
                 course_id: Optional[int] = None,
                 enrollment_date: Optional[str] = None,
                 course_name: Optional[str] = None):
        """
        Initialize an Enrollment object with provided attributes
        
        Args:
            enrollment_id: Unique identifier for the enrollment
            student_id: ID of the enrolled student
            course_id: ID of the enrolled course
            enrollment_date: Date of enrollment (YYYY-MM-DD)
            course_name: Name of the enrolled course (optional)
        """
        self._enrollment_id = enrollment_id
        self._student_id = student_id
        self._course_id = course_id
        self._enrollment_date = enrollment_date
        self._course_name = course_name

    # Property for enrollment_id
    @property
    def enrollment_id(self) -> Optional[int]:
        return self._enrollment_id
    
    @enrollment_id.setter
    def enrollment_id(self, value: int):
        if value <= 0:
            raise ValueError("Enrollment ID must be positive")
        self._enrollment_id = value

    # Property for student_id
    @property
    def student_id(self) -> Optional[int]:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value: int):
        if value <= 0:
            raise ValueError("Student ID must be positive")
        self._student_id = value

    # Property for course_id
    @property
    def course_id(self) -> Optional[int]:
        return self._course_id
    
    @course_id.setter
    def course_id(self, value: int):
        if value <= 0:
            raise ValueError("Course ID must be positive")
        self._course_id = value

    # Property for enrollment_date
    @property
    def enrollment_date(self) -> Optional[str]:
        return self._enrollment_date
    
    @enrollment_date.setter
    def enrollment_date(self, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError("Enrollment date must be in YYYY-MM-DD format")
        self._enrollment_date = value

    # Property for course_name
    @property
    def course_name(self) -> Optional[str]:
        return self._course_name
    
    @course_name.setter
    def course_name(self, value: str):
        if value is not None and len(value) > 100:
            raise ValueError("Course name cannot exceed 100 characters")
        self._course_name = value

    def __str__(self) -> str:
        return (f"Enrollment(ID: {self.enrollment_id}, "
                f"Student: {self.student_id}, "
                f"Course: {self.course_id or self.course_name})")

    def to_dict(self) -> dict:
        """Convert Enrollment object to dictionary"""
        return {
            'enrollment_id': self.enrollment_id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date,
            'course_name': self.course_name
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Enrollment':
        """Create Enrollment object from dictionary"""
        return cls(
            enrollment_id=data.get('enrollment_id'),
            student_id=data.get('student_id'),
            course_id=data.get('course_id'),
            enrollment_date=data.get('enrollment_date'),
            course_name=data.get('course_name')
        )