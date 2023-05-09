from urllib.parse import urljoin

from .core import process_response


class AddOnsMixin:
    @process_response
    def get_application_add_ons(self):
        url = urljoin(self.host, "addons")
        return self.make_request("GET", url)
