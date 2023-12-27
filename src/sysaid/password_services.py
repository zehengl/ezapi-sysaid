from urllib.parse import urljoin

from .core import process_response


class PasswordServicesMixin:
    @process_response
    def get_ldap_domains(self):
        url = urljoin(self.host, "ps/domain")
        return self.make_request("GET", url)

    @process_response
    def get_password_services_permission(self):
        url = urljoin(self.host, "ps/permission")
        return self.make_request("GET", url)
