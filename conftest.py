import os

from pyqaunicore import config_core
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

from config.config_general import config_general
from support.loggers.testrun_logger import logger

#Задание логгера ядра
config_core.logger = logger # LoggerLoguru(log_file_path=config_core.log_file_path)

# Определение значения переменной окружения для уровня логирования логгера и БД
config_general.log_deep_trace = os.environ.get('TESTS_LOG_DEEP_TRACE') in (1, '1', 'true', 'True')
if config_general.log_deep_trace:
    logger.set_file_log_level_as_deep_trace()

# -------------------------------------------
#   определение путей к файлам фикстур
# -------------------------------------------

pytest_plugins = [
    'testrunner.pytest_hooks',
    # 'pyqaunicore.ui.ui_engine.selene_bindings.selene_fixtures_web',  # добавить при использовании Selene
    # 'pyqaunicore.ui.ui_engine.selene_bindings.selene_fixtures_electron',  # добавить при использовании Selene с Electron
]
