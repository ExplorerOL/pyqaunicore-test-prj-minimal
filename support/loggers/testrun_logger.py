"""Модуль логгера"""

# Раскомментировать для логгера LoggerLoguru
from pyqaunicore.loggers.logger_loguru import LoggerLoguru

from config.config_general import config_general

logger = LoggerLoguru(config_general.log_file_path)

# Раскомментировать для логгера LoggerLogging
# from pyqaunicore.loggers.logger_logging import LoggerLogging

# logger = LoggerLogging(config_general.log_file_path)
