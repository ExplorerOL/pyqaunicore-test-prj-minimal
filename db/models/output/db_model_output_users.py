from pyqaunicore.validators.validator_pydantic import ValidatorPydantic

from db.models.input.db_model_input_users import DBModelInputUser


class DBModelOutputUser(DBModelInputUser, ValidatorPydantic.BaseModel):
    pass


class DBModelOutputUsers(ValidatorPydantic.RootModel):
    root: list[DBModelOutputUser]
