from pyqaunicore.api import GetValidCookiesFunc
from pyqaunicore.api.ws.datatypes.ws_datatypes import GetWSConnDataFunc
from pyqaunicore.api.ws.ws_client_item_websockets import WSClientItemWebsockets


class WSClientEndpoint(WSClientItemWebsockets):
    def __init__(
        self,
        uri: str,
        get_valid_cookies_func: GetValidCookiesFunc | None = None,
        get_conn_id_func: GetWSConnDataFunc | None = None,
    ):
        conn_uri = uri
        if get_conn_id_func is not None:
            conn_data = get_conn_id_func()
            conn_uri = f'{uri}?id={conn_data.connectionId}'
        super().__init__(uri=conn_uri, get_valid_cookies_func=get_valid_cookies_func)
