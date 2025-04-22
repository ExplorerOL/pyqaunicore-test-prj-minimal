"""Модуль для работы с данными скады в БД"""

from pyqaunicore.db.sql_db_client_item_base import SqlDBClientItemBase


class DBClientSql(SqlDBClientItemBase):
    """Класс для работы с SQL-запросами"""

    def exec_sql(self, sql_req: str, values_data: tuple[dict, ...] | None = None) -> tuple | None:
        """Выполнение SQL-запроса"""
        return self._db_adapter.exec_sql(sql_req=sql_req, values_data=values_data)
