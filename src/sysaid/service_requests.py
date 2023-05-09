from urllib.parse import urljoin

from requests.models import PreparedRequest

from .core import process_response


class ServiceRequestsMixin:
    @process_response
    def get_service_requests_list(self, **kwargs):
        url = urljoin(self.host, "sr")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    def get_all_service_requests(self):
        service_requests = []
        limit = 500
        num = 0
        while True:
            batch = self.get_service_requests_list(offset=num * limit, limit=limit)
            if not len(batch):
                break
            service_requests.extend(batch)
            num += 1
        return service_requests

    @process_response
    def get_service_request(self, service_request_id, **kwargs):
        url = urljoin(self.host, f"sr/{service_request_id}")
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)

    @process_response
    def search_service_requests(self, query, **kwargs):
        url = urljoin(self.host, f"cr/search")
        kwargs["query"] = query
        req = PreparedRequest()
        req.prepare_url(url, kwargs)
        url = req.url
        return self.make_request("GET", url)
