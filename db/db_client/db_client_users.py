"""Модуль для работы с данными скады в БД"""

from typing import Sequence

from pyqaunicore.db.sql_db_client_item_base import SqlDBClientItemBase

from db.models.input.db_model_input_users import DBModelInputUser


class DBClientUsers(SqlDBClientItemBase):
    """Класс для работы с данными пользователей в БД"""

    def create_user(self, user_data: DBModelInputUser | Sequence[DBModelInputUser]):
        """Создание пользователя в БД

        Параметры:
            user_data (DBModelInputUser): Модель пользователя
        """
        if isinstance(user_data, DBModelInputUser):
            user_data = [user_data]
        self._db_adapter.exec_insert(elems=tuple(user_data))

    def get_all_users(self) -> list[DBModelInputUser]:
        """Получение всех пользователей из БД

        Возвращаемые значения:
            tuple: Модель списка пользователей
        """
        statement = self._db_adapter.select_statement(DBModelInputUser)
        users = list(self._db_adapter.exec_select(statement))
        return users

    def delete_all_users(self):
        """Удаление всех пользователей из БД"""
        statement = self._db_adapter.delete_statement(DBModelInputUser)
        self._db_adapter.exec_truncate(statement=statement)
