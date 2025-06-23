import pytest 

def test_simple_add():
    assert 1+1 == 2

# @pytest.mark.xfail
# @pytest.mark.skip
# @pytest.mark.skipif(os.name == "posix", reason="does not work on mac")
def test_failing():
    assert 'a' == 'b'