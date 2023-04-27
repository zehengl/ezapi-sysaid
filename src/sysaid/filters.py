from urllib.parse import urljoin

from .core import process_response


class FiltersMixin:
    @process_response
    def get_filters_list(self):
        url = urljoin(self.host, "filters")

        return self.make_request("GET", url)

    @process_response
    def get_filter(self, filter_id):
        url = urljoin(self.host, f"filters/{filter_id}")

        return self.make_request("GET", url)
