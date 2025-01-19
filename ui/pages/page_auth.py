from typing import Self

from pyqaunicore.ui import PageBase
from pyqaunicore.ui.primitives import Button, Input
from pyqaunicore.ui.primitives.label import Label
from pyqaunicore.ui.ui_engine.ui_engine_base import UIEngineBase


class PageAuth(PageBase):
    S_INPUT_LOGIN = '[data-test="username"]'
    S_INPUT_PASSWORD = '[data-test="password"]'
    S_BTN_LOGIN = '[data-test="login-button"]'

    S_LBL_AUTH_ERROR = '[data-test="error"]'

    def __init__(self, page: UIEngineBase.Page, expect: UIEngineBase.Expect, url: str, title: str):
        super().__init__(page=page, expect=expect, url=url, title=title)

        self.__input_username = Input(
            page=self._page,
            selector=self.S_INPUT_LOGIN,
            expect=self._expect,
            name_in_log='Поле ввода имени пользователя',
        )
        self.__input_password = Input(
            page=self._page,
            selector=self.S_INPUT_PASSWORD,
            expect=self._expect,
            name_in_log='Поле ввода пароля',
        )
        self.__btn_login = Button(
            page=self._page,
            selector=self.S_BTN_LOGIN,
            expect=self._expect,
            name_in_log='Кнопка входа',
        )

        self.__lbl_auth_error = Label(
            page=self._page,
            selector=self.S_LBL_AUTH_ERROR,
            expect=self._expect,
            name_in_log='Надпись об ошибке авторизации',
        )

    ####### Actions #########

    def fill_username(self, username: str) -> Self:
        self.__input_username.fill(username)
        return self

    def fill_password(self, password: str) -> Self:
        self.__input_password.fill(password)
        return self

    def click_btn_login(self) -> Self:
        self.__btn_login.click()
        return self

    def login(self, username: str, password: str) -> None:
        self.fill_username(username).fill_password(password).click_btn_login()

    ####### Assertions #########

    def verify_auth_error_msg(self, expected_error: str) -> None:
        self.__lbl_auth_error.verify_is_visible()
        self.__lbl_auth_error.verify_has_text(expected_text=expected_error)

    def verify_main_elements_visible(self) -> None:
        self.__input_username.verify_is_visible()
        self.__input_password.verify_is_visible()
        self.__btn_login.verify_is_visible()
