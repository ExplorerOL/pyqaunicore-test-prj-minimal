import os

from pyqaunicore.config import config_core
from pyqaunicore.testrunners.pytest.pytest_hooks import (  # noqa: F401
    # импортировать используемые хуки pytest из ядра
    pytest_collection_modifyitems,
    pytest_exception_interact,
    pytest_fixture_post_finalizer,
    pytest_fixture_setup,
    pytest_make_parametrize_id,
    pytest_runtest_logfinish,
    pytest_runtest_logstart,
    pytest_runtest_makereport,
)

# раскомментировать при использовании Selene
from pyqaunicore.ui.ui_engine.bindings_selene.selene_fixtures_web import (
    browser,
    browser_context_args,
    browser_launch_options,
    context,
    pytest_addoption,
    view,
)

# раскомментировать при использовании Playwright
# from pyqaunicore.ui.ui_engine.bindings_playwright.playwright_fixtures_web import view
from support.loggers.testrun_logger import logger

# Задание логгера ядра
config_core.logger = logger

# Определение значения переменной окружения для уровня логирования логгера и БД
tests_log_level = os.environ.get('TESTS_LOG_LEVEL')
if tests_log_level is not None:
    logger.set_log_level(log_level=tests_log_level)

# -------------------------------------------
#   определение путей к файлам фикстур
# -------------------------------------------

pytest_plugins = [
    'testrunner.pytest_hooks',
]
