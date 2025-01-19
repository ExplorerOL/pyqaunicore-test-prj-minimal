from pyqaunicore.ui.datatypes.ui_datatypes import GetPageFunc
from pyqaunicore.ui.primitives.button import Button
from pyqaunicore.ui.primitives.container import Container
from pyqaunicore.ui.ui_engine.ui_engine_base import UIEngineBase


class MainMenuItems(Container):
    S_MENU_ITEM_ABOUT = '[data-test="about-sidebar-link"]'
    S_MENU_ITEM_LOGOUT = '[data-test="logout-sidebar-link"]'

    def __init__(
        self,
        page: UIEngineBase.Page | GetPageFunc,
        expect: UIEngineBase.Expect,
        selector: str,
        name_in_log: str | None = None,
    ):
        super().__init__(
            page=page,
            expect=expect,
            selector=selector,
            name_in_log=name_in_log,
        )

        self.__item_about = Button(
            page=page,
            expect=expect,
            selector=self.S_MENU_ITEM_ABOUT,
            text='About',
        )

        self.__item_logout = Button(
            page=page,
            expect=expect,
            selector=self.S_MENU_ITEM_LOGOUT,
            text='Logout',
        )

    def select_item_about(self) -> None:
        self.__item_about.click()

    def select_item_logout(self) -> None:
        self.__item_logout.click()
