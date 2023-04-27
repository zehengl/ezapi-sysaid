from urllib.parse import urljoin

from .core import process_response


class ListsMixin:
    @process_response
    def get_all_list(self):
        url = urljoin(self.host, "list")

        return self.make_request("GET", url)

    @process_response
    def get_list(self, list_id):
        url = urljoin(self.host, f"list/{list_id}")

        return self.make_request("GET", url)
