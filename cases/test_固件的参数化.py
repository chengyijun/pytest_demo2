import pytest

"""
与函数参数化使用 @pytest.mark.parametrize 不同，固件在定义时使用 params 参数进行参数化。
固件参数化依赖于内置固件 request 及其属性 param。
"""


@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def param(request):
    return request.param


@pytest.fixture(autouse=True)
def db(param):
    print('\nSucceed to connect %s:%s' % param)

    yield

    print('\nSucceed to close %s:%s' % param)


def test_api():
    assert 1 == 1
