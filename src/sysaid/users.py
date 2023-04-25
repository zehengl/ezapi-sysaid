from urllib.parse import urljoin

from .core import process_response


class UsersMixin:
    @process_response
    def get_users(self):
        url = urljoin(self.host, "users")

        return self.make_request("GET", url)
