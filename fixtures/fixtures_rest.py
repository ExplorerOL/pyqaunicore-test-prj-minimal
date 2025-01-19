import pytest
from pyqaunicore.api import HTTPClient, HTTPReqSenderBase
from pyqaunicore.api.rest.http_req_sender_requests import HTTPReqSenderRequests as HTTPReqSender

# from pyqaunicore.api import HTTPReqSenderHttpx as HTTPReqSender
from api.rest.rest_client import RESTClient

BASE_URL = 'https://reqres.in/'


@pytest.fixture(scope='session')
def http_req_sender() -> HTTPReqSenderBase:
    return HTTPReqSender()


@pytest.fixture(scope='session')
def http_client(http_req_sender) -> HTTPClient:
    return HTTPClient(http_req_sender=http_req_sender, base_url=BASE_URL)


@pytest.fixture(scope='session')
def rest_client_anonim(http_client) -> RESTClient:
    return RESTClient(http_client=http_client, auth_creds=None)
