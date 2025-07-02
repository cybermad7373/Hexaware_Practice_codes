import pytest
from exception.duplicate_enrollment_exception import DuplicateEnrollmentException
from exception.student_not_found_exception import StudentNotFoundException
from exception.course_not_found_exception import CourseNotFoundException

def test_enroll_student(sis_service, sample_student, sample_course):
    """Test enrolling a student in a course"""
    # Add student and course first
    student = sis_service.add_student(sample_student, "testpassword")
    course = sis_service.add_course(sample_course)
    
    # Test successful enrollment
    enrollment = sis_service.enroll_student(student.student_id, course.course_id)
    assert enrollment.enrollment_id is not None
    
    # Test duplicate enrollment
    with pytest.raises(DuplicateEnrollmentException):
        sis_service.enroll_student(student.student_id, course.course_id)
    
    # Test with non-existent student
    with pytest.raises(StudentNotFoundException):
        sis_service.enroll_student(99999, course.course_id)
    
    # Test with non-existent course
    with pytest.raises(CourseNotFoundException):
        sis_service.enroll_student(student.student_id, 99999)

def test_get_enrollments(sis_service, sample_student, sample_course):
    """Test retrieving student enrollments"""
    # Add student and course first
    student = sis_service.add_student(sample_student, "testpassword")
    course = sis_service.add_course(sample_course)
    
    # Enroll student
    sis_service.enroll_student(student.student_id, course.course_id)
    
    # Test getting enrollments
    enrollments = sis_service.get_enrollments_by_student(student.student_id)
    assert len(enrollments) == 1
    assert enrollments[0].course_id == course.course_id
    
    # Test with student having no enrollments
    new_student = sis_service.add_student(
        Student(first_name="New", last_name="Student", email="new@student.edu", 
                date_of_birth="2000-01-01", phone_number="9876543211"),
        "password"
    )
    enrollments = sis_service.get_enrollments_by_student(new_student.student_id)
    assert len(enrollments) == 0