import requests

from .login import LoginMixin

mixins = [
    LoginMixin,
]


class SysAid(*mixins):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        self.session = requests.Session()

    def make_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)
