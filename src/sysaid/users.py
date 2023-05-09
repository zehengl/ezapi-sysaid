from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class UsersMixin:
    @process_response
    def get_users_list(self, **kwargs):
        url = urljoin(self.host, "users")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    def get_all_users(self):
        users = []
        limit = 500
        num = 0
        while True:
            batch = self.get_users_list(offset=num * limit, limit=limit)
            if not len(batch):
                break
            users.extend(batch)
            num += 1
        return users

    @process_response
    def get_user(self, user_id, **kwargs):
        url = urljoin(self.host, f"users/{user_id}")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    @process_response
    def search_users(self, query, **kwargs):
        url = urljoin(self.host, f"users/search")
        kwargs["query"] = query
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    @process_response
    def get_user_permissions(self, user_id):
        url = urljoin(self.host, f"users/{user_id}/permission")
        return self.make_request("GET", url)
