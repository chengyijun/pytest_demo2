import pytest


@pytest.fixture(autouse=True)
def hello():
    print('我自动执行了')
    return 'hello'


def test_hello():
    assert True
