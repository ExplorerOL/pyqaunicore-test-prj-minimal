from support.validators.data_validator import DataValidator


class APIModelOutputUserInfo(DataValidator.BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class APIModelOutputUserSupport(DataValidator.BaseModel):
    url: str
    text: str


class APIModelOutputUser(DataValidator.BaseModel):
    data: APIModelOutputUserInfo
    support: APIModelOutputUserSupport
