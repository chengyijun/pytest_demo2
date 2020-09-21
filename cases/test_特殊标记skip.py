import pytest

a = 0


@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass


@pytest.mark.skipif(a > 1, reason='out-of-date api')
def test_connect2():
    pass
