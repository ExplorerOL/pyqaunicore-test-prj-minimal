import enum

from pyqaunicore.api.rest.models.rest_models import RESTModelResponse
from pyqaunicore.api.rest.rest_client_endpoint_base import RESTClientEndpointBase

from support.loggers.testrun_logger import logger


class EndpointsLogin(enum.StrEnum):
    LOGIN = 'api/login'


class RESTClientLogin(RESTClientEndpointBase):
    def login(self, email: str, password: str, verify_status_code: bool = True) -> RESTModelResponse:
        """Получение токена авторизации

        Args:
            auth_creds (AuthCreds): Данные авторизации пользователя
        Returns:
            Response: Объект HTTP-ответа
        """
        headers = {'Content-type': 'application/json'}
        body = f'{{"email": "{email}", "password": "{password}"}}'
        self._http_client.clear_cookies()
        response = self._http_client.post(
            EndpointsLogin.LOGIN, headers=headers, data=body, verify_status_code=verify_status_code
        )

        cookies = response.cookies
        logger.debug(f'Полученные куки: {cookies}')
        return response
