import requests

from .login import LoginMixin
from .users import UsersMixin

mixins = [
    LoginMixin,
    UsersMixin,
]


class SysAid(*mixins):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        self.session = requests.Session()

    def make_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)
