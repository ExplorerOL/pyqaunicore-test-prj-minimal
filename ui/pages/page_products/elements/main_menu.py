# from pyqaunicore.templates.prj_minimal.support.loggers.testrun_logger import logger
from pyqaunicore.ui.datatypes.ui_datatypes import GetPageFunc
from pyqaunicore.ui.elements.menu import Menu
from pyqaunicore.ui.ui_engine.ui_engine_base import UIEngineBase

from ui.pages.page_products.elements.main_menu_items import MainMenuItems


class MainMenu(Menu):
    S_MENU_ITEM = '[class="bm-item menu-item"]'
    S_MENU_ITEMS = '[class="bm-item-list"]'

    def __init__(
        self,
        page: UIEngineBase.Page | GetPageFunc,
        expect: UIEngineBase.Expect,
        selector: str,
        btn_open_close_selector: str,
        iframe_name: str | None = None,
        text: str | None = None,
        name_in_log: str | None = None,
    ):
        super().__init__(
            page=page,
            expect=expect,
            selector=selector,
            btn_open_close_selector=btn_open_close_selector,
            text=text,
            name_in_log=name_in_log,
        )

        self.__menu_items = MainMenuItems(
            page=page,
            expect=expect,
            selector=self.S_MENU_ITEMS,
        )

    def is_opened(self) -> bool:
        """Получить состояние открытого меню

        Возвращаемые значения:
            bool: Состояние открытого меню
        """
        return self.get_attribute('aria-hidden') == 'false'

    def get_items_count(self) -> int:
        """Количество элементов меню

        Возвращаемые значения:
            int: Количество элементов меню
        """
        return self._page.locator(self.S_MENU_ITEM).count()

    def get_items_names(self) -> list[str]:
        """Количество элементов меню

        Возвращаемые значения:
            int: Количество элементов меню
        """
        return [str(locator.text_content()).strip() for locator in self._page.locator(self.S_MENU_ITEM).all()]

    def is_btn_open_close_visible(self) -> bool:
        if self._btn_open_close.is_visible():
            return True
        return False

    def open(self, **kwargs) -> MainMenuItems:
        """Открыть меню

        Возвращаемые значения:
            Self: Объект c элементами меню
        """
        # logger.deep_trace('MainMenu -> open()')
        if not self.is_opened():
            self._btn_open_close.click()
            self.__menu_items.wait_for_visible()
            self.wait_for_timeout(timeout_ms=300)
        return self.__menu_items
