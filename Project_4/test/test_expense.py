import pytest
from datetime import datetime
from expense_tracker.expense_tracker import add_expense, get_monthly_summary, get_yearly_summary

def test_add_expense():
    """Test adding a new expense"""
    result = add_expense(150.75, "Transport", "Bus tickets")
    assert result is True

def test_get_monthly_summary():
    """Test retrieving monthly summary"""
    current_month = datetime.now().strftime('%Y-%m')
    summary = get_monthly_summary(current_month)
    assert isinstance(summary, list)
    if summary:  # If there are expenses this month
        assert all('category' in item and 'total' in item for item in summary)

def test_get_yearly_summary():
    """Test retrieving yearly summary"""
    current_year = datetime.now().strftime('%Y')
    summary = get_yearly_summary(current_year)
    assert isinstance(summary, list)
    if summary:  # If there are expenses this year
        assert all('month_year' in item and 'total' in item for item in summary)