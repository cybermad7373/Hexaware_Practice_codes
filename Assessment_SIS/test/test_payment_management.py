import pytest
from exception.payment_validation_exception import PaymentValidationException
from exception.student_not_found_exception import StudentNotFoundException
from exception.insufficient_funds_exception import InsufficientFundsException

def test_record_payment(sis_service, sample_student):
    """Test recording a payment"""
    # Add student first
    student = sis_service.add_student(sample_student, "testpassword")
    
    # Test successful payment
    payment = sis_service.record_payment(student.student_id, 5000.00)
    assert payment.payment_id is not None
    assert payment.amount == 5000.00
    
    # Test invalid amount
    with pytest.raises(PaymentValidationException):
        sis_service.record_payment(student.student_id, -100.00)
    
    # Test with non-existent student
    with pytest.raises(StudentNotFoundException):
        sis_service.record_payment(99999, 1000.00)

def test_get_payments(sis_service, sample_student):
    """Test retrieving payment history"""
    # Add student first
    student = sis_service.add_student(sample_student, "testpassword")
    
    # Record some payments
    sis_service.record_payment(student.student_id, 3000.00)
    sis_service.record_payment(student.student_id, 2000.00)
    
    # Test getting payments
    payments = sis_service.get_payments_by_student(student.student_id)
    assert len(payments) == 2
    assert sum(p.amount for p in payments) == 5000.00
    
    # Test with student having no payments
    new_student = sis_service.add_student(
        Student(first_name="New", last_name="Student", email="new@student.edu", 
                date_of_birth="2000-01-01", phone_number="9876543211"),
        "password"
    )
    payments = sis_service.get_payments_by_student(new_student.student_id)
    assert len(payments) == 0