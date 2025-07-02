from datetime import date
from typing import Optional
from util.validation_util import ValidationUtil

class Student:
    """Represents a student in the Student Information System"""
    
    def __init__(self, student_id: Optional[int] = None, 
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 date_of_birth: Optional[str] = None,
                 email: Optional[str] = None,
                 phone_number: Optional[str] = None):
        """
        Initialize a Student object with provided attributes
        
        Args:
            student_id: Unique identifier for the student
            first_name: Student's first name
            last_name: Student's last name
            date_of_birth: Student's date of birth (YYYY-MM-DD)
            email: Student's email address
            phone_number: Student's phone number
        """
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._email = email
        self._phone_number = phone_number

    # Property for student_id
    @property
    def student_id(self) -> Optional[int]:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value: int):
        if value <= 0:
            raise ValueError("Student ID must be positive")
        self._student_id = value

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

    # Property for date_of_birth
    @property
    def date_of_birth(self) -> Optional[str]:
        return self._date_of_birth
    
    @date_of_birth.setter
    def date_of_birth(self, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError("Date of birth must be in YYYY-MM-DD format")
        self._date_of_birth = value

    # Property for email
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @email.setter
    def email(self, value: str):
        if not ValidationUtil.validate_email(value):
            raise ValueError("Invalid email format")
        self._email = value.lower().strip()

    # Property for phone_number
    @property
    def phone_number(self) -> Optional[str]:
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value: str):
        if not ValidationUtil.validate_phone(value):
            raise ValueError("Invalid phone number format")
        self._phone_number = value.strip()

    def __str__(self) -> str:
        return f"Student(ID: {self.student_id}, Name: {self.first_name} {self.last_name}, Email: {self.email})"

    def to_dict(self) -> dict:
        """Convert Student object to dictionary"""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'phone_number': self.phone_number
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Create Student object from dictionary"""
        return cls(
            student_id=data.get('student_id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            date_of_birth=data.get('date_of_birth'),
            email=data.get('email'),
            phone_number=data.get('phone_number')
        )