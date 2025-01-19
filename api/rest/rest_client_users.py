import enum

from pyqaunicore.api.rest.models.rest_models import RESTModelResponse
from pyqaunicore.api.rest.rest_client_endpoint_base import RESTClientEndpointBase
from pyqaunicore.operations.operations_url import OperationsUrl


class EndpointsUsers(enum.StrEnum):
    USERS = 'api/users'


class RESTClientUsers(RESTClientEndpointBase):
    def get_single_user(self, user_id: int, verify_status_code: bool = True) -> RESTModelResponse:
        response = self._http_client.get(
            EndpointsUsers.USERS + '/' + str(user_id), verify_status_code=verify_status_code
        )
        return response

    def get_list_users(self, page: int, verify_status_code: bool = True) -> RESTModelResponse:
        quety_params_str = OperationsUrl.convert_dict_to_query_params({'page': str(page)})
        response = self._http_client.get(
            EndpointsUsers.USERS + quety_params_str, verify_status_code=verify_status_code
        )
        return response
