"""Модуль логгера"""

# Раскомментировать для логгера LoggerLoguru
from pyqaunicore.loggers.logger_loguru import LoggerLoguru as TestrunLogger

# Раскомментировать для логгера LoggerLogging
# from pyqaunicore.loggers.logger_logging import LoggerLogging as TestrunLogger
from config.config_general import config_general

logger = TestrunLogger(config_general.log_file_path)
