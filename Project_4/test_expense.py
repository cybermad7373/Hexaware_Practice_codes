import pytest
from datetime import date
from expense_tracker import ExpenseTracker

@pytest.fixture
def tracker():
    et = ExpenseTracker()
    et.expenses.clear()  # Clear sample data
    et.categories.clear()
    et.add_expense(100.0, "Food", date(2023, 1, 15))
    et.add_expense(200.0, "Transport", date(2023, 1, 20))
    return et

def test_add_expense(tracker):
    assert len(tracker.expenses[(1, 2023)]) == 2
    tracker.add_expense(300.0, "Food", date(2023, 2, 10))
    assert len(tracker.expenses[(2, 2023)]) == 1

def test_monthly_summary(tracker):
    assert tracker.monthly_summary(1, 2023) == 300.0
    assert tracker.monthly_summary(2, 2023) == 0.0

def test_yearly_summary(tracker):
    assert tracker.yearly_summary(2023) == 300.0
    tracker.add_expense(300.0, "Food", date(2023, 2, 10))
    assert tracker.yearly_summary(2023) == 600.0

def test_category_spending(tracker):
    categories = tracker.category_spending()
    assert categories["Food"] == 100.0
    assert categories["Transport"] == 200.0