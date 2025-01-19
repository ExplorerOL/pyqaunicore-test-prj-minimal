import datetime

from pyqaunicore.validators.validator_pydantic import ValidatorPydantic

# from pyqaunicore.templates.prj_minimal.db.db_provider import DBProvider
from db.models.input.db_model_input_users import DBModelInputUser


class DBModelOutputUser(DBModelInputUser, ValidatorPydantic.BaseModel):
    # __table_args__: Optional[dict] = {'schema': 'dbo'}
    # __tablename__: str | None = 'users'
    id: int | None = None
    name: str
    age: int
    created_at: int = int(datetime.datetime.now().timestamp())
    is_deleted: bool = False
    is_blocked: bool = False


class DBModelOutputUsers(ValidatorPydantic.RootModel):
    root: list[DBModelOutputUser]
