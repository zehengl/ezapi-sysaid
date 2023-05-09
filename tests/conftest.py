from os import getenv

import pytest
from dotenv import load_dotenv

from sysaid import SysAid

load_dotenv()


@pytest.fixture()
def sysaid():
    host = getenv("sysaid_host", "http://localhost/api/v1/")
    username = getenv("sysaid_username", "username")
    password = getenv("sysaid_password", "password")

    return SysAid(host, username, password, login=False)
