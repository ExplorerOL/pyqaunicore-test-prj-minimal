import datetime

# from pyqaunicore.templates.prj_minimal.db.db_provider import DBProvider
from db.db_adapter import SqlDBAdapter


class DBModelInputUser(SqlDBAdapter.SQLModel, table=True):
    """Модель роли в БД"""

    # __table_args__: Optional[dict] = {'schema': 'dbo'}
    __tablename__: str | None = 'users'
    id: int | None = SqlDBAdapter.Field(default=None, primary_key=True)
    name: str
    age: int
    created_at: int = int(datetime.datetime.now().timestamp())
    is_deleted: bool = False
    is_blocked: bool = False
