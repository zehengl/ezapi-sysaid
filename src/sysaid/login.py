from urllib.parse import urljoin

from .core import process_response


class LoginMixin:
    @process_response
    def login(self):
        url = urljoin(self.host, "login")
        data = {
            "user_name": self.username,
            "password": self.password,
        }

        return self.make_request("POST", url, json=data)
