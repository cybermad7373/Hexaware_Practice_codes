from abc import ABC, abstractmethod
from entity.student import Student
from entity.course import Course
from entity.enrollment import Enrollment
from entity.teacher import Teacher
from entity.payment import Payment

class SISService(ABC):
    """Abstract base class defining the SIS service interface"""
    
    @abstractmethod
    def add_student(self, student: Student, password: str) -> Student:
        pass
    
    @abstractmethod
    def get_student(self, student_id: int) -> Student:
        pass
    
    @abstractmethod
    def authenticate_student(self, email: str, password: str) -> Student:
        pass
    
    @abstractmethod
    def update_student(self, student: Student) -> bool:
        pass
    
    @abstractmethod
    def add_course(self, course: Course) -> Course:
        pass
    
    @abstractmethod
    def get_course(self, course_id: int) -> Course:
        pass
    
    @abstractmethod
    def assign_teacher_to_course(self, teacher_id: int, course_id: int) -> bool:
        pass
    
    @abstractmethod
    def enroll_student(self, student_id: int, course_id: int) -> Enrollment:
        pass
    
    @abstractmethod
    def get_enrollments_by_student(self, student_id: int) -> list[Enrollment]:
        pass
    
    @abstractmethod
    def record_payment(self, student_id: int, amount: float) -> Payment:
        pass
    
    @abstractmethod
    def get_payments_by_student(self, student_id: int) -> list[Payment]:
        pass
    
    @abstractmethod
    def generate_enrollment_report(self, course_id: int) -> dict:
        pass
    
    @abstractmethod
    def generate_payment_report(self, student_id: int) -> dict:
        pass