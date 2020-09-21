import pytest

"""
作用域是指固件的作用域
session > module > class > funciton
session 一次测试任务 只执行一次
module 一个模块里面只执行一次
class 一个类里面只执行一次
function 一个函数执行一次
"""


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    print('初始化')

    yield

    print('收尾工作')


# def test_multi_scope(sess_scope, mod_scope, func_scope):
#     pass
#
#
# def test_multi_scope2(sess_scope, mod_scope, func_scope):
#     pass

@pytest.mark.skip
@pytest.mark.usefixtures('sess_scope', 'mod_scope', 'class_scope')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass


class TestClassScope2:

    def setup_class(self):
        print('初始化测试环境')

    def teardown_class(self):
        print('恢复测试环境')

    def test_1(self):
        pass

    def test_2(self):
        pass
