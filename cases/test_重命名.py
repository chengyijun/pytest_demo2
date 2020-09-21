import pytest

"""
给固件指定一个别名  测试函数可以通过固件的别名进行调用
"""


@pytest.fixture(name='age')
def calculate_average_age():
    return 28


def test_age(age):
    assert age == 28
