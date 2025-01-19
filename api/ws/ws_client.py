import enum

from api.ws.ws_client_echo import WSClientEndpoint


class WSEndpoints(enum.StrEnum):
    WS_ECHO_ENDPOINT = 'https://echo.websocket.org/echo'
    WS_EVENTS_ENDPOINT = 'https://echo.websocket.org/events'


class WSClient:
    def __init__(self):
        self.echo = WSClientEndpoint(uri=WSEndpoints.WS_ECHO_ENDPOINT)
        self.events = WSClientEndpoint(uri=WSEndpoints.WS_EVENTS_ENDPOINT)
