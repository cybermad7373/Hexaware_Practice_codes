import pytest
import json
from Project_4.quiz import (
    create_quiz,
    add_question,
    take_quiz,
    calculate_score
)

def test_create_quiz():
    """Test creating a new quiz"""
    quiz_id = create_quiz("General Knowledge")
    assert isinstance(quiz_id, int)
    assert quiz_id > 0

def test_add_question():
    """Test adding a question to a quiz"""
    quiz_id = create_quiz("Science Quiz")
    options = json.dumps(["A. Option 1", "B. Option 2", "C. Option 3"])
    result = add_question(quiz_id, "What is H2O?", options, "B. Option 2")
    assert result is True

def test_take_quiz():
    """Test retrieving a quiz with questions"""
    quiz_id = create_quiz("Math Quiz")
    options = json.dumps(["A. 1", "B. 2", "C. 3", "D. 4"])
    add_question(quiz_id, "1 + 1 = ?", options, "B. 2")
    
    quiz = take_quiz(quiz_id)
    assert quiz is not None
    assert quiz['quiz_name'] == "Math Quiz"
    assert len(quiz['questions']) == 1
    assert "1 + 1 = ?" in quiz['questions'][0]['question']

def test_calculate_score():
    """Test the score calculation lambda"""
    assert calculate_score(8, 10) == 80.0
    assert calculate_score(5, 5) == 100.0
    assert calculate_score(0, 10) == 0.0
    assert calculate_score(3, 0) == 0.0  # Edge case - division by zero handled