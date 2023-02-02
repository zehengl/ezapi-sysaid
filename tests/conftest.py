import pytest

from sysaid import SysAid


@pytest.fixture()
def sysaid():
    username = "username"
    password = "password"

    return SysAid(username, password)
