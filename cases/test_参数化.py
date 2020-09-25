import pytest


@pytest.mark.skip
@pytest.mark.parametrize('passwd',
                         ['123456',
                          'abcdefdfs',
                          'as52345fasdf4'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8


@pytest.mark.skip
@pytest.mark.parametrize('user, passwd',
                         [('jack', 'abcdefgh'),
                          ('tom', 'a123456a')])
def test_passwd_md5(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }

    import hashlib

    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]


@pytest.mark.parametrize('name',
                         ['abel'])
def test_csh(name):
    print(name)
    assert len(name) >= 2
