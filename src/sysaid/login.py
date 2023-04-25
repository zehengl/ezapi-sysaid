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
        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }

        return self.make_request("POST", url, headers=headers, data=data)
