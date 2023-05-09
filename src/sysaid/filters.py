from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class FiltersMixin:
    @process_response
    def get_filters_list(self, **kwargs):
        url = urljoin(self.host, "filters")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    def get_all_filters(self):
        filters = []
        limit = 500
        num = 0
        while True:
            batch = self.get_filters_list(offset=num * limit, limit=limit)
            if not len(batch):
                break
            filters.extend(batch)
            num += 1
        return filters

    @process_response
    def get_filter(self, filter_id, **kwargs):
        url = urljoin(self.host, f"filters/{filter_id}")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)
