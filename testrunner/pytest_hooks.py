"""Модуль с хуками тестраннера для проекта"""

from config import config_init


def pytest_configure(config):
    """Хук конфигурации pytest"""
    config_init.init_config(config)
    config_init.init_reporter(config)
