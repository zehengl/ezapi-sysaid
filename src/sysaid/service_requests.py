from urllib.parse import urljoin

from .core import process_response


class ServiceRequestsMixin:
    @process_response
    def get_service_requests_list(self):
        url = urljoin(self.host, "sr")

        return self.make_request("GET", url)

    @process_response
    def get_service_request(self, service_request_id):
        url = urljoin(self.host, f"sr/{service_request_id}")

        return self.make_request("GET", url)
