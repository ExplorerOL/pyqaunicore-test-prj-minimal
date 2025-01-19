import pytest
from pyqaunicore.reporters.pytest_html.pytest_html_functions import Reporter

from config.config_general import config_general
from support.loggers.testrun_logger import logger


def init_config(config):
    """Инициализация конфигурации тестового прогона"""

    # инициализация базовых глобальных переменных и объектов, которые нужны
    # для формирования отчета (еще до вызова фикстуры global_vars)

    # инициализация pytest.BASE_URL для использования при получении версии ПО
    # добавлении ее в названия отчета. Фикстура base_url здесь еще не доступна
    # и при вызове с опцией --collect-only возникает ошибка

    config_general.base_url = config.option.base_url
    logger.debug('Конфигурация базового url: ' + config_general.base_url)

    # rest_steps = APIProvider.get_rest_steps(
    #     base_url=config_general.base_url,
    #     auth_creds=ScadaUsers.user_system.auth_creds,
    # )

    # # try:
    # scada_info = rest_steps.info.get_scada_info()
    # config_general.sw_version = scada_info.version
    # logger.debug(f'Версия сборки: {config_general.sw_version}')
    # config_general.scada_server_os_type = scada_info.service['os']
    # logger.debug(f'Тип ОС: {config_general.scada_server_os_type}')
    # # except (KeyError, ValueError, ConnectionError) as error:
    # #     print("Ошибка:", error)
    # #     pytest.fail("Ошибка получения информации о скаде для отчета!")

    # # задание пути для html-отчета
    # config.option.htmlpath = f'{config_general.reports_dir}/report-WebScadaMT-{config_general.sw_version}-{config_general.scada_server_os_type}.html'
    # # задание пути для xml-отчета
    # config.option.xmlpath = f'{config_general.reports_dir}/report-WebScadaMT-{config_general.sw_version}-{config_general.scada_server_os_type}.xml'

    # # обработка опции --scada-path
    # custom_scada_path = config.getoption('--scada-path')
    # if custom_scada_path is not None:
    #     config_general.scada_path = custom_scada_path

    # # определение разницы времени между тестирующим ПК и сервером скады
    # config_general.scada_server_time_delta = calculate_scada_server_time_delta()

    # # изменение параметров конфигурации если OC сервера скады Linux
    # if config_general.is_scada_server_os_linux:
    #     config_general.scada_path = '/var/lib/webscadamt'
    #     config_general.scada_db_backup_path = '/var/lib/webscadamt/Backup/database'

    # # конвертация проектов для ОС Linux и изменение имен файлов проектов в конфигурации
    # config_general.SMOKE_PRJ_NAME = (
    #     MTPTool(config_general.TEST_PRJ_DIR_PATH / (config_general.SMOKE_PRJ_NAME + '.mtp'))
    #     .convert_prj_for_linux()
    #     .stem
    # )
    # config_general.REGRESS_PRJ_NAME = (
    #     MTPTool(config_general.TEST_PRJ_DIR_PATH / (config_general.REGRESS_PRJ_NAME + '.mtp'))
    #     .convert_prj_for_linux()
    #     .stem
    # )


# def calculate_scada_server_time_delta() -> datetime.timedelta:
#     scada_server_time_delta = datetime.timedelta(seconds=0)
#     rest_steps = APIProvider.get_rest_client(
#         base_url=config_general.base_url,
#         auth_creds=ScadaUsers.user_system.auth_creds,
#     )
#     try:
#         response = rest_steps.params.get_parameters_by_mid_sid(mid=ScadaModules.system_modules.HOST.id)
#     except (KeyError, ValueError, ConnectionError) as error:
#         logger.debug(f'Ошибка: {error}')
#         pytest.fail('Ошибка получения времени сервера скады!')
#     assert response.status_code == 200

#     testing_pc_time = datetime.datetime.now()
#     host_params_list = json.loads(response.text)
#     for param in host_params_list:
#         if param['n'] == 'HOST.CurrentTime':
#             scada_server_time_str = str(param['v'])[:-2]
#             scada_server_time_utc = datetime.datetime.strptime(scada_server_time_str, '%Y-%m-%dT%H:%M:%S.%f')
#             scada_server_time_delta = (
#                 scada_server_time_utc + response.elapsed + config_general.TIME_DELTA_FROM_UTC
#             ) - testing_pc_time
#     return scada_server_time_delta


def init_reporter(pytest_config) -> None:
    """Инициализация параметров репортера

    Параметры:
        pytest_config (_type_): параметры Pytest
    """
    Reporter.report_title = config_general.report_title
    Reporter.aut_info_for_report_dict = config_general.aut_info_for_report_dict
    Reporter.add_host_environment_data_and_sw_info_into_report(pytest_config)

    # добавление атрибута с путем для скриншотов для плагина pytest-playwright-visual в объект pytest
    setattr(pytest, 'snapshot_failures_path', config_general.failed_tests_snapshots_path)
