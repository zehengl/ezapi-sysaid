from urllib.parse import urljoin

from .core import process_response


class ActionItemsMixin:
    @process_response
    def get_action_items(self):
        url = urljoin(self.host, "action_item")

        return self.make_request("GET", url)
