import pytest


def fun(x):
    if not isinstance(x, int):
        raise TypeError('x不是数字')
    elif x != 100:
        raise ValueError('x值不对')


def test_raises():
    with pytest.raises(ValueError) as e:
        fun(101)
    exec_msg = e.value.args[0]
    print(exec_msg)
    assert exec_msg == 'x值不对'
