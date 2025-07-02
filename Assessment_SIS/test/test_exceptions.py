import pytest
from exception.duplicate_enrollment_exception import DuplicateEnrollmentException
from exception.course_not_found_exception import CourseNotFoundException
from exception.student_not_found_exception import StudentNotFoundException
from exception.teacher_not_found_exception import TeacherNotFoundException
from exception.payment_validation_exception import PaymentValidationException
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.invalid_data_exception import InvalidStudentDataException

def test_duplicate_enrollment_exception():
    """Test DuplicateEnrollmentException"""
    exc = DuplicateEnrollmentException(101, 201)
    assert str(exc) == "Student 101 is already enrolled in course 201"
    assert exc.student_id == 101
    assert exc.course_id == 201

def test_course_not_found_exception():
    """Test CourseNotFoundException"""
    exc = CourseNotFoundException("CS101")
    assert str(exc) == "Course not found: CS101"
    assert exc.course_identifier == "CS101"

def test_student_not_found_exception():
    """Test StudentNotFoundException"""
    exc = StudentNotFoundException(101)
    assert str(exc) == "Student not found: 101"
    assert exc.student_identifier == 101

def test_teacher_not_found_exception():
    """Test TeacherNotFoundException"""
    exc = TeacherNotFoundException("teacher@example.com")
    assert str(exc) == "Teacher not found: teacher@example.com"
    assert exc.teacher_identifier == "teacher@example.com"

def test_payment_validation_exception():
    """Test PaymentValidationException"""
    exc = PaymentValidationException("Negative amount", {"amount": -100})
    assert str(exc) == "Payment validation failed: Negative amount"
    assert exc.payment_data == {"amount": -100}

def test_insufficient_funds_exception():
    """Test InsufficientFundsException"""
    exc = InsufficientFundsException(101, 5000.00, 3000.00)
    assert str(exc) == ("Student 101 has insufficient funds. "
                       "Required: 5000.00, Available: 3000.00")
    assert exc.student_id == 101
    assert exc.required_amount == 5000.00
    assert exc.available_amount == 3000.00

def test_invalid_student_data_exception():
    """Test InvalidStudentDataException"""
    exc = InvalidStudentDataException("email", "bad-email", "Invalid format")
    assert str(exc) == "Invalid student data: email='bad-email' - Invalid format"
    assert exc.field_name == "email"
    assert exc.field_value == "bad-email"
    assert exc.reason == "Invalid format"