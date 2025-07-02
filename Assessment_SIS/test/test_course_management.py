import pytest
from exception.course_not_found_exception import CourseNotFoundException
from exception.invalid_data_exception import InvalidCourseDataException
from exception.teacher_not_found_exception import TeacherNotFoundException

def test_add_course(sis_service, sample_course, sample_teacher):
    """Test adding a new course"""
    # Add a teacher first
    teacher = sis_service.add_teacher(sample_teacher)
    
    # Test successful addition
    sample_course.teacher_id = teacher.teacher_id
    added_course = sis_service.add_course(sample_course)
    assert added_course.course_id is not None
    
    # Test duplicate course code
    with pytest.raises(Exception, match="Duplicate entry"):
        sis_service.add_course(sample_course)

def test_get_course(sis_service, sample_course):
    """Test retrieving a course"""
    # Add a course first
    added_course = sis_service.add_course(sample_course)
    
    # Test successful retrieval
    retrieved = sis_service.get_course(added_course.course_id)
    assert retrieved.course_id == added_course.course_id
    assert retrieved.course_code == sample_course.course_code
    
    # Test not found
    with pytest.raises(CourseNotFoundException):
        sis_service.get_course(99999)

def test_course_validation():
    """Test course model validation"""
    course = Course()
    
    # Test invalid course name
    with pytest.raises(InvalidCourseDataException):
        course.course_name = ""
    
    # Test invalid credits
    with pytest.raises(InvalidCourseDataException):
        course.credits = 7

def test_assign_teacher(sis_service, sample_course, sample_teacher):
    """Test assigning teacher to course"""
    # Add a course and teacher first
    added_course = sis_service.add_course(sample_course)
    added_teacher = sis_service.add_teacher(sample_teacher)
    
    # Test successful assignment
    result = sis_service.assign_teacher_to_course(added_teacher.teacher_id, added_course.course_id)
    assert result is True
    
    # Test with non-existent teacher
    with pytest.raises(TeacherNotFoundException):
        sis_service.assign_teacher_to_course(99999, added_course.course_id)
    
    # Test with non-existent course
    with pytest.raises(CourseNotFoundException):
        sis_service.assign_teacher_to_course(added_teacher.teacher_id, 99999)