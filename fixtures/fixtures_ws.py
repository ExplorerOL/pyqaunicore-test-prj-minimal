import pytest

from api.ws.ws_client import WSClient


@pytest.fixture(scope='session')
def ws_client_anonim() -> WSClient:
    ws_client = WSClient()
    ws_client.echo.receive_msg(timeout_ms=20000)
    ws_client.events.receive_msg(timeout_ms=20000)
    return ws_client
