import datetime

from pyqaunicore.generators.generators_number import GeneratorsNumber
from pyqaunicore.generators.generators_string import GeneratorsString

from api.ws.ws_client import WSClient
from fixtures.fixtures_ws import ws_client_anonim  # noqa: F401
from support.loggers.testrun_logger import logger


class TestExamplesWS:
    def test_get_echo_answer(self, ws_client_anonim: WSClient):  # noqa: F811
        """Получение ответа от сервера"""
        # ARRANGE
        MSG_TEXT = GeneratorsString.generate_random_string(
            length=GeneratorsNumber.generate_random_int(min_val=1, max_val=100)
        )
        logger.debug(MSG_TEXT)
        # ACT
        ws_client_anonim.echo.send_msg(msg=MSG_TEXT)
        response = ws_client_anonim.echo.receive_msg(timeout_ms=20000)
        # ASSERT
        assert response == MSG_TEXT

    def test_get_last_event(self, ws_client_anonim: WSClient):  # noqa: F811
        """Получение последнего события"""
        # ARRANGE
        MSG_TEXT = str(datetime.datetime(2022, 1, 1, 1, 1, 1, tzinfo=datetime.timezone.utc))
        # ACT
        ws_client_anonim.events.send_msg(msg=MSG_TEXT)
        response = ws_client_anonim.events.receive_msg(timeout_ms=20000)
        # ASSERT
        assert response == MSG_TEXT
