from dataclasses import dataclass

# from fixtures.fixtures_ui import ui_client  # noqa: F401
from support.loggers.testrun_logger import logger
from ui.ui_client import UIClient

pytest_plugins = ('fixtures.fixtures_ui',)


@dataclass(frozen=True, slots=True)
class AuthCreds:
    username: str
    password: str


creds_locked_user = AuthCreds(username='locked_out_user', password='secret_sauce')
creds_standart_user = AuthCreds(username='standard_user', password='secret_sauce')


class TestExamplesUI:
    def test_auth_locked_user(self, ui_client: UIClient):  # noqa: F811
        """Авторизация заблокированного пользователя"""
        # ARRANGE
        ERROR_TEXT = 'Epic sadface: Sorry, this user has been locked out.'
        # ACT
        ui_client.page_auth.navigate().login(
            username=creds_locked_user.username,
            password=creds_locked_user.password,
        )
        # ASSERT
        ui_client.page_auth.verify_url()
        ui_client.page_auth.verify_title()
        ui_client.page_auth.verify_auth_error_msg(expected_error=ERROR_TEXT)

    def test_auth_standart_user(self, ui_client: UIClient):  # noqa: F811
        """Авторизация стандартного пользователя"""
        # ARRANGE
        SHOP_NAME = 'Swag Labs'
        # ACT
        ui_client.page_auth.navigate().login(
            username=creds_standart_user.username,
            password=creds_standart_user.password,
        )
        # ASSERT
        ui_client.page_products.verify_url()
        ui_client.page_products.verify_title()
        ui_client.page_products.verify_lbl_shop_name_text(expected_shop_name=SHOP_NAME)

    def test_product_card_data(self, ui_client: UIClient):  # noqa: F811
        """Данные карточки продукта"""
        # ARRANGE
        PRODUCT_NAME = 'Sauce Labs Bolt T-Shirt'
        PRODUCT_DESC = 'Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.'
        PRODUCT_PRICE = '$15.99'
        ui_client.page_auth.navigate().login(
            username=creds_standart_user.username,
            password=creds_standart_user.password,
        )
        # ACT
        product_card3 = ui_client.page_products.get_product_card_by_index(index=3)
        # ASSERT
        product_card3.verify_is_visible()
        product_card3.verify_product_name(expected_name=PRODUCT_NAME)
        product_card3.verify_product_desc(expected_desc=PRODUCT_DESC)
        product_card3.verify_product_price(expected_price=PRODUCT_PRICE)

    def test_visible_products_count(self, ui_client: UIClient):  # noqa: F811
        """Количество видимых карточек товаров"""
        # ARRANGE
        EXPECTED_CARDS_COUNT = 6
        ui_client.page_auth.navigate().login(
            username=creds_standart_user.username,
            password=creds_standart_user.password,
        )
        # ACT
        visible_products_count = ui_client.page_products.get_products_cards_count()
        logger.info(f'Количество видимых карточек товаров: {visible_products_count}')
        # ASSERT
        assert visible_products_count == EXPECTED_CARDS_COUNT, (
            'Количество видимых карточек товаров не соответствует ожидаемому!'
        )

    def test_get_all_product_cards(self, ui_client: UIClient):  # noqa: F811
        """Названия всех продуктов в карточках"""
        # ARRANGE
        PRODUCT_NAMES = (
            'Sauce Labs Backpack',
            'Sauce Labs Bike Light',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Fleece Jacket',
            'Sauce Labs Onesie',
            'Test.allTheThings() T-Shirt (Red)',
        )
        ui_client.page_auth.navigate().login(
            username=creds_standart_user.username,
            password=creds_standart_user.password,
        )
        # ACT
        product_cards = ui_client.page_products.get_all_products_cards()
        # ASSERT
        for index, product_card in enumerate(product_cards):
            product_card.verify_product_name(expected_name=PRODUCT_NAMES[index])

    def test_logout_using_menu(self, ui_client: UIClient):  # noqa: F811
        """Выход из сеанса с помощью элемента меню"""
        # ARRANGE
        ui_client.page_auth.navigate().login(
            username=creds_standart_user.username,
            password=creds_standart_user.password,
        )
        # ACT
        ui_client.page_products.open_main_menu().select_item_logout()
        # ASSERT
        ui_client.page_auth.verify_url()
        ui_client.page_auth.verify_title()
        ui_client.page_auth.verify_main_elements_visible()
