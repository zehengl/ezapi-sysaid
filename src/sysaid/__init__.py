import requests

from .action_items import ActionItemsMixin
from .add_ons import AddOnsMixin
from .assets import AssetsMixin
from .filters import FiltersMixin
from .lists import ListsMixin
from .login import LoginMixin
from .password_services import PasswordServicesMixin
from .service_requests import ServiceRequestsMixin
from .users import UsersMixin

mixins = [
    ActionItemsMixin,
    AddOnsMixin,
    AssetsMixin,
    FiltersMixin,
    ListsMixin,
    LoginMixin,
    PasswordServicesMixin,
    ServiceRequestsMixin,
    UsersMixin,
]


class SysAid(*mixins):
    def __init__(self, host, username, password, login=True):
        self.host = host
        self.username = username
        self.password = password

        self.session = requests.Session()

        if login:
            self.login()

    def make_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)
