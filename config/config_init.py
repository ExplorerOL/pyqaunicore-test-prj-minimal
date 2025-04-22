import pytest
from pyqaunicore.reporters.pytest_html.reporter_pytest_html import ReporterPytestHtml

from config.config_general import config_general
from support.loggers.testrun_logger import logger


def init_config(config):
    """Инициализация конфигурации тестового прогона"""

    config_general.base_url = config.option.base_url
    logger.debug('Конфигурация базового url: ' + config_general.base_url)


def init_reporter(pytest_config) -> None:
    """Инициализация параметров репортера

    Параметры:
        pytest_config (_type_): параметры Pytest
    """
    ReporterPytestHtml.report_title = config_general.report_title
    ReporterPytestHtml.aut_info_for_report_dict = config_general.aut_info_for_report_dict
    ReporterPytestHtml.add_host_environment_data_and_sw_info_into_report(pytest_config)

    # добавление атрибута с путем для скриншотов для плагина pytest-asser-screenshot в объект pytest
    setattr(pytest, 'screenshot_failures_path', config_general.failed_tests_screenshots_path)
