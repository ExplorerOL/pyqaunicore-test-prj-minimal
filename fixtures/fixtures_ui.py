import pytest

from config.config_general import config_general
from ui.pages.page_auth import PageAuth
from ui.pages.page_products.page_products import PageProducts
from ui.ui_engine import UIEngine


@pytest.fixture
def page_auth(page):
    return PageAuth(
        page=page,
        expect=UIEngine.Expect(),  # type: ignore
        url=config_general.base_url,
        title='Swag Labs',
    )


@pytest.fixture
def page_products(page):
    return PageProducts(
        page=page,
        expect=UIEngine.Expect(),  # type: ignore
        url=f'{config_general.base_url}inventory.html',
        title='Swag Labs',
    )
