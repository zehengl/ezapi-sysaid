from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class ListsMixin:
    @process_response
    def get_all_list(self, **kwargs):
        url = urljoin(self.host, "list")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)
