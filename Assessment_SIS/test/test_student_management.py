import pytest
from exception.student_not_found_exception import StudentNotFoundException
from exception.invalid_data_exception import InvalidStudentDataException

def test_add_student(sis_service, sample_student):
    """Test adding a new student"""
    # Test successful addition
    added_student = sis_service.add_student(sample_student, "testpassword123")
    assert added_student.student_id is not None
    
    # Test duplicate email
    with pytest.raises(ValueError, match="Email already registered"):
        sis_service.add_student(sample_student, "testpassword123")

def test_get_student(sis_service, sample_student):
    """Test retrieving a student"""
    # Add a student first
    added_student = sis_service.add_student(sample_student, "testpassword123")
    
    # Test successful retrieval
    retrieved = sis_service.get_student(added_student.student_id)
    assert retrieved.student_id == added_student.student_id
    assert retrieved.email == sample_student.email
    
    # Test not found
    with pytest.raises(StudentNotFoundException):
        sis_service.get_student(99999)

def test_student_validation():
    """Test student model validation"""
    student = Student()
    
    # Test invalid first name
    with pytest.raises(InvalidStudentDataException):
        student.first_name = ""
    
    # Test invalid email
    with pytest.raises(InvalidStudentDataException):
        student.email = "invalid-email"
    
    # Test invalid date format
    with pytest.raises(InvalidStudentDataException):
        student.date_of_birth = "01-01-2000"

def test_authenticate_student(sis_service, sample_student):
    """Test student authentication"""
    # Add a student first
    added_student = sis_service.add_student(sample_student, "correctpassword")
    
    # Test successful authentication
    authenticated = sis_service.authenticate_student(sample_student.email, "correctpassword")
    assert authenticated.student_id == added_student.student_id
    
    # Test wrong password
    with pytest.raises(ValueError, match="Invalid password"):
        sis_service.authenticate_student(sample_student.email, "wrongpassword")
    
    # Test non-existent email
    with pytest.raises(StudentNotFoundException):
        sis_service.authenticate_student("nonexistent@email.com", "anypassword")