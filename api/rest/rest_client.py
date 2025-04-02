from pyqaunicore.api.http.http_client import HTTPClient
from pyqaunicore.api.rest.rest_client_base import RESTClientBase
from pyqaunicore.models.auth.models_auth import ModelAuthUsernamePassword

from api.rest.rest_client_login import RESTClientLogin
from api.rest.rest_client_users import RESTClientUsers


class RESTClient(RESTClientBase):
    def __init__(
        self,
        http_client: HTTPClient,
        auth_creds: ModelAuthUsernamePassword | None,
    ):
        super().__init__(http_client=http_client, auth_creds=auth_creds)
        self.auth = RESTClientLogin(http_client=http_client)
        self.users = RESTClientUsers(http_client=http_client)
