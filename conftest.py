import pytest

"""
conftest.py 是pytest框架集中管理固件的地方 
文件名约定为这个conftest.py不可更改
用例会自动导入并调用这个文件里的固件，不需要显式指定
"""


@pytest.fixture()
def postcode():
    return '010'


@pytest.fixture()
def hi():
    return 'hi'


def pytest_addoption(parser):
    parser.addoption('--host', action='store', default="localhost",
                     help='host of db')
    parser.addoption('--port', action='store', default='8888',
                     help='port of db')
