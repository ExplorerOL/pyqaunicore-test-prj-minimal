"""Модуль UI-клиента"""

from pyqaunicore.ui import UIEngineProtocol
from pyqaunicore.ui.ui_client_base import UIClientBase

from config.config_general import config_general
from config.constants import TestAppPagesUrls
from ui.pages.page_auth import PageAuth
from ui.pages.page_products.page_products import PageProducts


class UIClient(UIClientBase):
    """Класс UI-клиента"""

    _view: UIEngineProtocol.View

    def __init__(
        self,
        expect: UIEngineProtocol.Expect,
        view: UIEngineProtocol.View,
    ):
        super().__init__()
        self.logger.deep_trace('Инициализация UI-клиента')
        self.set_view(view=view)
        self.page_auth = PageAuth(
            view=self.get_view,
            expect=expect,
            url=f'{config_general.base_url}{TestAppPagesUrls.PAGE_AUTH}',
            title='Swag Labs',
        )
        self.page_products = PageProducts(
            view=self.get_view,
            expect=expect,
            url=f'{config_general.base_url}{TestAppPagesUrls.PAGE_PRODUCTS}',
            title='Swag Labs',
        )
