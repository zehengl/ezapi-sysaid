from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class ResourceBundleMixin:
    @process_response
    def get_rb_translated_keys(self, **kwargs):
        url = urljoin(self.host, "rb")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)
