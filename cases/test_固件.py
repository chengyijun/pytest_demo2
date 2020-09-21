import pytest

"""
所谓固件实际是指
讲一个函数作为参数传递到测试函数中，从而达代码的复用
"""


@pytest.mark.skip
def test_postcode(postcode):
    assert postcode == '010'





def test_hi(hi):
    assert hi == 'hi'
