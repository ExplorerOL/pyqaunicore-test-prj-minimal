from dataclasses import dataclass

import pytest
from pyqaunicore.operations.operations_file import OperationsFile

# from fixtures.fixtures_ui import page_auth, page_products  # noqa: F401
from support.loggers.testrun_logger import logger
from ui.ui_client import UIClient


@dataclass(frozen=True, slots=True)
class AuthCreds:
    username: str
    password: str


creds_locked_user = AuthCreds(username='locked_out_user', password='secret_sauce')
creds_standart_user = AuthCreds(username='standard_user', password='secret_sauce')


class TestExamplesVisual:
    def test_visual_auth_page(self, ui_client: UIClient, assert_screenshot):  # noqa: F811
        """Визуальный тест страницы авторизации"""
        # ARRANGE
        ui_client.page_auth.navigate()
        # ACT
        screenshot_page_auth = ui_client.page_auth.make_screenshot()
        # ASSERT
        screenshot_name = OperationsFile.generate_screenshot_name()
        logger.debug('Имя базового скриншота = ' + screenshot_name)
        assert_screenshot(
            screenshot_page_auth,
            threshold=0.12,
            name=screenshot_name,
            fail_fast=False,
        )

    @pytest.mark.xfail(reason='Тест демонстрации отчета визуального тестирования')
    def test_visual_auth_page_failed(self, ui_client: UIClient, assert_screenshot):  # noqa: F811
        """Провальный тест страницы авторизации"""
        # ARRANGE
        ui_client.page_auth.navigate()
        # ACT
        screenshot_page_auth = ui_client.page_auth.make_screenshot()
        # ASSERT
        screenshot_name = OperationsFile.generate_screenshot_name()
        logger.debug('Имя базового скриншота = ' + screenshot_name)
        assert_screenshot(
            screenshot_page_auth,
            threshold=0.12,
            name=screenshot_name,
            fail_fast=False,
        )
