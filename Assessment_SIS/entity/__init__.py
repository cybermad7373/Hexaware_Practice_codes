# Marks this directory as a Python package
from .student import Student
from .course import Course
from .enrollment import Enrollment
from .teacher import Teacher
from .payment import Payment

__all__ = ['Student', 'Course', 'Enrollment', 'Teacher', 'Payment']