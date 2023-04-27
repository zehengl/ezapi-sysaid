from urllib.parse import urljoin

from .core import process_response


class AssetsMixin:
    @process_response
    def get_assets_list(self):
        url = urljoin(self.host, "asset")

        return self.make_request("GET", url)

    @process_response
    def get_asset(self, asset_id):
        url = urljoin(self.host, f"asset/{asset_id}")

        return self.make_request("GET", url)
