import pytest
from report_card import ReportCardSystem

@pytest.fixture
def rc_system():
    rcs = ReportCardSystem()
    # Mock user input for adding student
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('builtins.input', side_effect=["Alice", "90 85 95"])
        rcs.add_student()
    return rcs

def test_calculate_percentage(rc_system):
    assert rc_system.calculate_percentage([90, 85, 95]) == 90.0
    assert rc_system.calculate_percentage([70, 80, 90]) == 80.0

def test_get_grade(rc_system):
    assert rc_system.get_grade(95) == "A"
    assert rc_system.get_grade(85) == "B"
    assert rc_system.get_grade(75) == "C"

def test_generate_report(rc_system):
    report = rc_system.generate_report("Alice")
    assert report['percentage'] == 90.0
    assert report['grade'] == "A"