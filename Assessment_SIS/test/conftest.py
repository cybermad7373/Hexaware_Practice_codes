import pytest
from dao.sis_service_impl import SISServiceImpl
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher

@pytest.fixture
def sis_service():
    """Fixture providing a clean SIS service instance for each test"""
    with SISServiceImpl() as service:
        yield service

@pytest.fixture
def sample_student():
    """Fixture providing a sample student object"""
    return Student(
        first_name="Test",
        last_name="Student",
        date_of_birth="2000-01-01",
        email="test.student@university.edu",
        phone_number="9876543210"
    )

@pytest.fixture
def sample_course():
    """Fixture providing a sample course object"""
    return Course(
        course_name="Test Course",
        course_code="TEST101",
        credits=3
    )

@pytest.fixture
def sample_teacher():
    """Fixture providing a sample teacher object"""
    return Teacher(
        first_name="Test",
        last_name="Teacher",
        email="test.teacher@university.edu"
    )