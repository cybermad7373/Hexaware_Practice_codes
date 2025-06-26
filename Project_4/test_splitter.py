import pytest
from unittest.mock import patch
from splitter import BillSplitter

@pytest.fixture 
def splitter():
    s = BillSplitter()
    
    s.participants = {"Alice": 0.0, "Bob": 0.0}
    return s

def test_split_equal(splitter):  
    total = 100.0
    splitter.split_equal(total)  
    assert splitter.participants["Alice"] == 50.0
    assert splitter.participants["Bob"] == 50.0

@patch('builtins.input', side_effect=["60", "40"])
def test_split_by_percentage(mock_input, splitter):
    total = 100.0
    splitter.split_by_percentage(total)
    assert splitter.participants["Alice"] == 60.0
    assert splitter.participants["Bob"] == 40.0