import pytest
from Project_4.splitter import (
    create_bill,
    add_bill_share,
    get_bill_summary,
    equal_split,
    percentage_split
)

def test_create_bill():
    """Test creating a new bill"""
    bill_id = create_bill(250.00, "Dinner at Restaurant")
    assert isinstance(bill_id, int)
    assert bill_id > 0

def test_add_bill_share():
    """Test adding a share to a bill"""
    bill_id = create_bill(100.00)
    result = add_bill_share(bill_id, "Alice", 50.00)
    assert result is True

def test_get_bill_summary():
    """Test retrieving a bill summary"""
    bill_id = create_bill(300.00, "Hotel Stay")
    add_bill_share(bill_id, "Bob", 150.00)
    add_bill_share(bill_id, "Charlie", 150.00)
    
    summary = get_bill_summary(bill_id)
    assert summary is not None
    assert summary['bill']['total_amount'] == 300.00
    assert len(summary['shares']) == 2

def test_equal_split():
    """Test the equal split lambda function"""
    splits = equal_split(100, 4)
    assert len(splits) == 4
    assert all(x == 25 for x in splits)
    assert sum(splits) == 100

def test_percentage_split():
    """Test the percentage split lambda function"""
    percentages = [50, 30, 20]
    splits = percentage_split(200, percentages)
    assert len(splits) == 3
    assert splits == [100, 60, 40]
    assert sum(splits) == 200