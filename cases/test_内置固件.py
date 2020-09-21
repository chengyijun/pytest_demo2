import pytest


@pytest.mark.skip
def test_tmpdir(tmpdir):
    a_dir = tmpdir.mkdir('mytmpdir')
    print(a_dir)
    a_file = a_dir.join('tmpfile.txt')

    a_file.write('hello, pytest!')

    assert a_file.read() == 'hello, pytest!'


def test_option1(pytestconfig):
    print('host: %s' % pytestconfig.getoption('host'))
    print('port: %s' % pytestconfig.getoption('port'))
