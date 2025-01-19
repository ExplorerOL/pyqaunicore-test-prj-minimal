import pytest
from pyqaunicore.generators.generators import GeneratorsNumber

from db.db_client.db_client import DBClient
from db.models.input.db_model_input_users import DBModelInputUser
from db.models.output.db_model_output_users import (
    DBModelOutputUser,
    DBModelOutputUsers,
)
from fixtures.fixtures_db import (  # noqa: F401
    create_empty_user_table,
    db_adapter,
    db_client,
)


def creating_users_imitation(db_client: DBClient) -> list[DBModelOutputUser]:  # noqa: F811
    users_count = GeneratorsNumber.generate_random_int(min_val=2, max_val=10)
    users = [DBModelInputUser(name=f'User{i}', age=20 + i) for i in range(users_count)]
    validated_users = DBModelOutputUsers.model_validate(users).root
    db_client.users.create_user(user_data=users)
    return validated_users


class TestExamplesDB:
    @pytest.mark.usefixtures('create_empty_user_table')
    def test_verify_data_in_db(self, db_client: DBClient):  # noqa: F811
        # ARRANGE
        # Действия выполняются в фикстуре create_empty_user_table
        # ACT
        # Действия через UI или API. Здесь - имитация действий.
        created_users = creating_users_imitation(db_client=db_client)
        # ASSERT
        actual_users_raw = db_client.users.get_all_users()
        actual_users = DBModelOutputUsers.model_validate(actual_users_raw).root

        assert len(created_users) == len(
            actual_users_raw
        ), 'Количество пользователей в БД не равно ожидаемому!'
        for expected_user, actual_user in list(zip(created_users, actual_users)):
            assert expected_user.name == actual_user.name
            assert expected_user.age == actual_user.age
