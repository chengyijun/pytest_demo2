import pytest

"""
配合 -m 标记名  进行筛选执行用例
例如：pytest cases\test_标记.py -m finished
"""


@pytest.mark.smoke
@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.unfinished
def test_func2():
    assert 1 != 1


@pytest.mark.wait
def test_func3():
    assert 1 != 1
