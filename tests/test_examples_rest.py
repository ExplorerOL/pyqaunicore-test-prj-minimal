import json
from http import HTTPStatus

from pyqaunicore.assertions import assert_soft

from api.rest.rest_client import RESTClient
from fixtures.fixtures_rest import (  # noqa: F401
    http_client,
    http_req_sender,
    rest_client_anonim,
)


class TestExamplesREST:
    def test_auth_successfull(self, rest_client_anonim: RESTClient):  # noqa: F811
        # ARRANGE
        EMAIL = 'eve.holt@reqres.in'
        PASSWORD = 'cityslicka'
        # ACT
        response = rest_client_anonim.auth.login(email=EMAIL, password=PASSWORD)
        # ASSERT
        response_json = json.loads(response.text)
        assert response_json['token'] == 'QpwL5tke4Pnpja7X4'

    def test_get_single_user_data(self, rest_client_anonim: RESTClient):  # noqa: F811
        # ARRANGE
        USER_ID = 10
        # ACT
        response = rest_client_anonim.users.get_single_user(user_id=USER_ID)
        # ASSERT
        body = json.loads(response.text)
        with assert_soft:
            assert body['data']['id'] == USER_ID, 'Поле id не соответствует ожидаемому'
        with assert_soft:
            assert body['data'].get('email'), 'Отсутствует поле email'

    def test_get_single_user_data_with_wrong_id(self, rest_client_anonim: RESTClient):  # noqa: F811
        # ARRANGE
        USER_ID = 10000
        # ACT
        response = rest_client_anonim.users.get_single_user(user_id=USER_ID, verify_status_code=False)
        # ASSERT
        assert (
            response.status_code == HTTPStatus.NOT_FOUND
        ), f'Статус код не соответствует {HTTPStatus.NOT_FOUND}'

    def test_get_single_user_list(self, rest_client_anonim: RESTClient):  # noqa: F811
        # ARRANGE
        PAGE_NUM = 2
        # ACT
        response = rest_client_anonim.users.get_list_users(page=PAGE_NUM)
        # ASSERT
        body = json.loads(response.text)
        with assert_soft:
            assert (
                body['page'] == PAGE_NUM
            ), f'Фактическое зачение поля page {body["page"]} не соответствует ожидаемому {PAGE_NUM}'
        users_data = body['data']
        with assert_soft:
            assert len(users_data) == 6, 'Количество пользователей не соответствует ожидаемому'
