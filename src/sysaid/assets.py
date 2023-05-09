from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class AssetsMixin:
    @process_response
    def get_assets_list(self, **kwargs):
        url = urljoin(self.host, "asset")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    @process_response
    def get_asset(self, asset_id):
        url = urljoin(self.host, f"asset/{asset_id}")

        return self.make_request("GET", url)
