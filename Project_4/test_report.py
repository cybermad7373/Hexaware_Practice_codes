import pytest
from report_card import ReportCardSystem

@pytest.fixture
def rc_system():
    rcs = ReportCardSystem()
    # Directly inject test data
    rcs.students = {
        "Alice": {'marks': [90, 85, 95], 'date_added': "2023-01-01"},
        "Bob": {'marks': [70, 75, 80], 'date_added': "2023-01-01"}
    }
    return rcs

def test_calculate_percentage(rc_system):
    assert rc_system.calculate_percentage([90, 90, 90]) == 90.0
    assert rc_system.calculate_percentage([100, 80]) == 90.0

def test_get_grade(rc_system):
    assert rc_system.get_grade(95) == "A"
    assert rc_system.get_grade(85) == "B"
    assert rc_system.get_grade(75) == "C"

def test_generate_report(rc_system):
    report = rc_system.generate_report("Alice")
    assert report['percentage'] == pytest.approx(90.0)
    assert report['grade'] == "A"

def test_highest_scorer(rc_system):
    highest = rc_system.get_highest_scorer()
    assert highest[0] == "Alice"
    assert highest[1]['marks'] == [90, 85, 95]