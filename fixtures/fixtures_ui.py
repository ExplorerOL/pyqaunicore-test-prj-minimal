import pytest

from ui.ui_client import UIClient
from ui.ui_engine import UIEngine


@pytest.fixture(scope='session')
def expect():
    return UIEngine.Expect()


@pytest.fixture
def ui_client(expect, view):
    ui_client = UIClient(expect=expect, view=view)
    return ui_client
