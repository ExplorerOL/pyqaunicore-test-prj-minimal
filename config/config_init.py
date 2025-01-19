import pytest
from pyqaunicore.reporters.pytest_html.pytest_html_functions import Reporter

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
    Reporter.report_title = config_general.report_title
    Reporter.aut_info_for_report_dict = config_general.aut_info_for_report_dict
    Reporter.add_host_environment_data_and_sw_info_into_report(pytest_config)

    # добавление атрибута с путем для скриншотов для плагина pytest-playwright-visual в объект pytest
    setattr(pytest, 'snapshot_failures_path', config_general.failed_tests_snapshots_path)
