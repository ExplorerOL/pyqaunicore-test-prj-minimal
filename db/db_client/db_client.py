"""Модуль для работы с данными скады в БД"""

from db.db_adapter import SqlDBAdapter
from db.db_client.db_client_sql import DBClientSql
from db.db_client.db_client_users import DBClientUsers
from support.loggers.testrun_logger import logger


class DBClient:
    """Класс для работы с данными скады в БД"""

    def __init__(self, db_adapter: SqlDBAdapter):
        logger.debug('Инициализация клиента БД')
        self.sql = DBClientSql(db_adapter=db_adapter)
        self.users = DBClientUsers(db_adapter=db_adapter)
