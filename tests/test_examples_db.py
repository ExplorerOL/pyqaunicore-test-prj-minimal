import copy
from itertools import zip_longest

import pytest
from pyqaunicore.assertions import assert_soft
from pyqaunicore.generators.generators import GeneratorsNumber

from db.db_client.db_client import DBClient
from db.models.db_models_users import DBModelUser
from fixtures.fixtures_db import (  # noqa: F401
    create_empty_user_table,
    db_adapter,
    db_client,
)
from support.loggers.testrun_logger import logger


def creating_users_imitation(db_client: DBClient) -> list[DBModelUser]:  # noqa: F811
    users_count = GeneratorsNumber.generate_random_int(min_val=2, max_val=10)
    users = [DBModelUser(name=f'User{i}', age=20 + i) for i in range(users_count)]
    db_client.users.create_user(user_data=users)
    return users


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

        assert len(created_users) == len(
            actual_users_raw
        ), 'Количество пользователей в БД не равно ожидаемому!'

        for expected_user, actual_user in list(zip_longest(created_users, actual_users_raw)):
            with assert_soft:
                assert expected_user.name == actual_user.name
            with assert_soft:
                assert expected_user.age == actual_user.age
