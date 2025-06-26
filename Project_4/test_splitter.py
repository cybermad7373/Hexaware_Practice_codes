import pytest
from splitter import BillSplitter

@pytest.fixture
def splitter():
    return BillSplitter()

def test_split_equal(splitter):
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('builtins.input', side_effect=["Alice", "Bob", "", "100"])
        splitter.run()
        assert splitter.participants["Alice"] == 50.0
        assert splitter.participants["Bob"] == 50.0

def test_split_by_percentage(splitter):
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('builtins.input', side_effect=["Alice", "Bob", "", "100", "60", "40"])
        splitter.run()
        assert splitter.participants["Alice"] == 60.0
        assert splitter.participants["Bob"] == 40.0