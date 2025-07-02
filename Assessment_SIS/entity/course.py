from typing import Optional

class Course:
    """Represents a course in the Student Information System"""
    
    def __init__(self, course_id: Optional[int] = None,
                 course_name: Optional[str] = None,
                 course_code: Optional[str] = None,
                 credits: Optional[int] = None,
                 teacher_id: Optional[int] = None,
                 teacher_name: Optional[str] = None):
        """
        Initialize a Course object with provided attributes
        
        Args:
            course_id: Unique identifier for the course
            course_name: Name of the course
            course_code: Code of the course
            credits: Number of credits for the course
            teacher_id: ID of the teacher assigned to the course
            teacher_name: Name of the teacher assigned to the course
        """
        self._course_id = course_id
        self._course_name = course_name
        self._course_code = course_code
        self._credits = credits
        self._teacher_id = teacher_id
        self._teacher_name = teacher_name

    # Property for course_id
    @property
    def course_id(self) -> Optional[int]:
        return self._course_id
    
    @course_id.setter
    def course_id(self, value: int):
        if value <= 0:
            raise ValueError("Course ID must be positive")
        self._course_id = value

    # Property for course_name
    @property
    def course_name(self) -> Optional[str]:
        return self._course_name
    
    @course_name.setter
    def course_name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Course name cannot be empty")
        if len(value) > 100:
            raise ValueError("Course name cannot exceed 100 characters")
        self._course_name = value.strip()

    # Property for course_code
    @property
    def course_code(self) -> Optional[str]:
        return self._course_code
    
    @course_code.setter
    def course_code(self, value: str):
        if not value or not value.strip():
            raise ValueError("Course code cannot be empty")
        if len(value) > 20:
            raise ValueError("Course code cannot exceed 20 characters")
        self._course_code = value.strip().upper()

    # Property for credits
    @property
    def credits(self) -> Optional[int]:
        return self._credits
    
    @credits.setter
    def credits(self, value: int):
        if not (1 <= value <= 6):
            raise ValueError("Credits must be between 1 and 6")
        self._credits = value

    # Property for teacher_id
    @property
    def teacher_id(self) -> Optional[int]:
        return self._teacher_id
    
    @teacher_id.setter
    def teacher_id(self, value: int):
        if value is not None and value <= 0:
            raise ValueError("Teacher ID must be positive")
        self._teacher_id = value

    # Property for teacher_name
    @property
    def teacher_name(self) -> Optional[str]:
        return self._teacher_name
    
    @teacher_name.setter
    def teacher_name(self, value: str):
        if value is not None and len(value) > 100:
            raise ValueError("Teacher name cannot exceed 100 characters")
        self._teacher_name = value

    def __str__(self) -> str:
        return f"Course(ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code})"

    def to_dict(self) -> dict:
        """Convert Course object to dictionary"""
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_code': self.course_code,
            'credits': self.credits,
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher_name
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Course':
        """Create Course object from dictionary"""
        return cls(
            course_id=data.get('course_id'),
            course_name=data.get('course_name'),
            course_code=data.get('course_code'),
            credits=data.get('credits'),
            teacher_id=data.get('teacher_id'),
            teacher_name=data.get('teacher_name')
        )