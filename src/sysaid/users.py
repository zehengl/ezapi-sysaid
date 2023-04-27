from urllib.parse import urljoin

from .core import process_response


class UsersMixin:
    @process_response
    def get_users_list(self):
        url = urljoin(self.host, "users")

        return self.make_request("GET", url)

    @process_response
    def get_user(self, user_id):
        url = urljoin(self.host, f"users/{user_id}")

        return self.make_request("GET", url)
