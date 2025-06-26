import pytest
from unittest.mock import patch
from quiz import QuizApp

@pytest.fixture
def quiz():
    q = QuizApp()
    q.score = 0
    return q

@patch('builtins.input', return_value="Paris")
def test_ask_question_correct(mock_input, quiz):
    quiz.ask_question("What is the capital of France?", "Paris")
    assert quiz.score == 1

@patch('builtins.input', return_value="London")
def test_ask_question_incorrect(mock_input, quiz):
    quiz.ask_question("What is the capital of France?", "Paris")
    assert quiz.score == 0

def test_run_quiz_resets_score(quiz):
    quiz.score = 5
    with patch('builtins.input', return_value="Paris"):
        quiz.run_quiz()
    assert quiz.score == 0