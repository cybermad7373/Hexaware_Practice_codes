import pytest
from unittest.mock import patch
from quiz import QuizApp

@pytest.fixture
def quiz():
    q = QuizApp()
    q.questions = {"Test Q": "Test A"}  # Simplified for testing
    return q

@patch('builtins.input', return_value="Test A")
def test_ask_question_correct(mock_input, quiz):
    quiz.ask_question("Test Q", "Test A")
    assert quiz.score == 1

@patch('builtins.input', return_value="Wrong")
def test_ask_question_incorrect(mock_input, quiz):
    quiz.ask_question("Test Q", "Test A")
    assert quiz.score == 0

def test_run_quiz_resets_score(quiz):
    quiz.score = 5
    with patch('builtins.input', return_value="Test A"):
        with patch.object(quiz, 'questions', {"Test Q": "Test A"}):
            quiz.run_quiz()
    assert quiz.score == 1  # Score should be 1 after running quiz