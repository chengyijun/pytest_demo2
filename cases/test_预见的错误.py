import pytest

a = 15


@pytest.mark.xfail(a > 10,
                   reason='not supported until v0.2.0')
def test_api():
    assert 1 == 1
