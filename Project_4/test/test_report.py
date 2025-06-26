import pytest
from Project_4.report_card import (
    add_student, 
    add_marks, 
    generate_report_card, 
    calculate_grade
)

def test_add_student():
    """Test adding a new student"""
    student_id = add_student("John Doe", "10A")
    assert isinstance(student_id, int)
    assert student_id > 0

def test_add_marks():
    """Test adding marks for a student"""
    student_id = add_student("Jane Smith", "9B")
    result = add_marks(student_id, "Math", 85.5)
    assert result is True

def test_generate_report_card():
    """Test generating a report card"""
    student_id = add_student("Test Student", "11C")
    add_marks(student_id, "Science", 92)
    add_marks(student_id, "History", 78)
    
    report = generate_report_card(student_id)
    assert report is not None
    assert report['student']['name'] == "Test Student"
    assert len(report['marks']) == 2
    assert report['stats']['average'] == 85.0

def test_calculate_grade():
    """Test the grade calculation lambda"""
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(75) == 'C'
    assert calculate_grade(65) == 'D'
    assert calculate_grade(55) == 'F'