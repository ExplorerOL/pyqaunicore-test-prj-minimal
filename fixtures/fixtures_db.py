import pytest
from pyqaunicore.db.sql_db_adapter_protocol import SqlDBAdapterProtocol
from pyqaunicore.db.sql_db_adapter_sqlmodel import SqlDBAdapterSQLModel

from config.config_general import config_general
from db.db_client.db_client import DBClient


@pytest.fixture(scope='session')
def db_adapter() -> SqlDBAdapterProtocol:
    return SqlDBAdapterSQLModel(conn_data=config_general.db_conn_string, debug=False)


@pytest.fixture(scope='session')
def db_client(db_adapter) -> DBClient:
    return DBClient(db_adapter=db_adapter)


# Создание тестовой таблицы
@pytest.fixture(scope='session')
def create_empty_user_table(db_client: DBClient) -> None:
    db_client.sql.exec_sql(
        sql_req="""
                            CREATE TABLE IF NOT EXISTS "users" (
                                "id"  INTEGER,
                                "name"  TEXT NOT NULL,
                                "age" INTEGER,
                                "created_at" INTEGER,
                                "is_deleted" BOOLEAN,
                                "is_blocked" BOOLEAN,
                                PRIMARY KEY("id")
                            );
                            """
    )
    db_client.users.delete_all_users()
