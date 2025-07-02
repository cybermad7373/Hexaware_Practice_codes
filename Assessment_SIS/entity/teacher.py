from typing import Optional
from util.validation_util import ValidationUtil

class Teacher:
    """Represents a teacher in the Student Information System"""
    
    def __init__(self, teacher_id: Optional[int] = None,
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 email: Optional[str] = None):
        """
        Initialize a Teacher object with provided attributes
        
        Args:
            teacher_id: Unique identifier for the teacher
            first_name: Teacher's first name
            last_name: Teacher's last name
            email: Teacher's email address
        """
        self._teacher_id = teacher_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    # Property for teacher_id
    @property
    def teacher_id(self) -> Optional[int]:
        return self._teacher_id
    
    @teacher_id.setter
    def teacher_id(self, value: int):
        if value <= 0:
            raise ValueError("Teacher ID must be positive")
        self._teacher_id = value

    # Property for first_name
    @property
    def first_name(self) -> Optional[str]:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str):
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        if len(value) > 50:
            raise ValueError("First name cannot exceed 50 characters")
        self._first_name = value.strip()

    # Property for last_name
    @property
    def last_name(self) -> Optional[str]:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        if len(value) > 50:
            raise ValueError("Last name cannot exceed 50 characters")
        self._last_name = value.strip()

    # Property for email
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @email.setter
    def email(self, value: str):
        if not ValidationUtil.validate_email(value):
            raise ValueError("Invalid email format")
        self._email = value.lower().strip()

    def __str__(self) -> str:
        return f"Teacher(ID: {self.teacher_id}, Name: {self.first_name} {self.last_name})"

    def to_dict(self) -> dict:
        """Convert Teacher object to dictionary"""
        return {
            'teacher_id': self.teacher_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Teacher':
        """Create Teacher object from dictionary"""
        return cls(
            teacher_id=data.get('teacher_id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email')
        )