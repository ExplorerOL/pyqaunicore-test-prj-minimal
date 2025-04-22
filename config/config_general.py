"""Модуль глобальной конфигурации тестов"""

import shutil
from pathlib import Path


class ConfigGeneral:
    """Класс хранения глобальных настроек"""

    def __init__(self):
        self._base_url = 'https://www.saucedemo.com/'
        self._reports_dir = Path('./reports')
        self.__tests_screenshots_dir = self._reports_dir.joinpath('screenshot_tests_failures')
        self.__log_file_path = self._reports_dir.joinpath('testrun_log.log')
        self.__log_deep_trace = False
        self.__db_conn_string = 'sqlite:///.database.db'
        self.report_title = 'Custom report title'
        self.aut_info_for_report_dict = {'Info1': 'Value1', 'Info2': 'Value2'}

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url):
        self._base_url = url

    @property
    def log_file_path(self):
        return self.__log_file_path

    @property
    def failed_tests_screenshots_path(self):
        return self.__tests_screenshots_dir

    @property
    def log_deep_trace(self):
        return self.__log_deep_trace

    @log_deep_trace.setter
    def log_deep_trace(self, deep_trace: bool):
        self.__log_deep_trace = deep_trace

    @property
    def db_conn_string(self) -> str:
        return self.__db_conn_string

    def clear_reports_directory(self):
        """Очистка директории для отчетов, кроме файла логов.

        Удаление самой директории иногда вызывает ошибку доступа из-за того, что операция удаления длительная,
        и, видимо, асинхронная. При этом уже создается новый файл лога loguru. И операция удаления не может
        завершиться нормально. Файл отчета управляется loguru - очищается при начале логирования.
        """
        if self._reports_dir.exists():
            for item in self._reports_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    if item != self.__log_file_path:
                        item.unlink()


config_general = ConfigGeneral()
