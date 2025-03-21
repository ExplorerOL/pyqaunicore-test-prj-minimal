from pyqaunicore.exceptions.exceptions_common import NotExpectedValueError
from pyqaunicore.ui import PageBase
from pyqaunicore.ui.primitives import Label
from pyqaunicore.ui.ui_engine.protocols.ui_engine_protocol import UIEngineProtocol

from ui.pages.page_products.elements.main_menu import MainMenu
from ui.pages.page_products.elements.main_menu_items import MainMenuItems
from ui.pages.page_products.elements.product_card import ProductCard


class PageProducts(PageBase):
    S_LBL_SHOP_NAME = '[class="app_logo"]'
    S_PRODUCT_CARD = '[data-test="inventory-item"]'
    S_CARDS_COLLECTION = '[data-test="inventory-container"]'
    S_CARD_ADDITION_TEMPLATE = ':nth-child({index})'

    S_BTN_OPEN_MENU = '[id="react-burger-menu-btn"]'
    S_MENU = '[class="bm-menu-wrap"]'

    def __init__(self, view: UIEngineProtocol.View, expect: UIEngineProtocol.Expect, url: str, title: str):
        super().__init__(view=view, expect=expect, url=url, title=title)

        self.__lbl_shop_name = Label(
            view=self._view,
            selector=self.S_LBL_SHOP_NAME,
            expect=self._expect,
            name_in_log='Надпись названия магазина',
        )
        self._main_menu = MainMenu(
            view=self._view,
            selector=self.S_MENU,
            expect=self._expect,
            btn_open_close_selector=self.S_BTN_OPEN_MENU,
            name_in_log='Меню товаров',
        )

    def get_products_cards_count(self) -> int:
        product_cart = ProductCard(view=self._view, expect=self._expect, selector=self.S_PRODUCT_CARD)
        return product_cart.count()

    def get_product_card_by_index(self, index: int) -> ProductCard:
        if index <= 0:
            raise NotExpectedValueError('Номер карточки должен быть больше нуля')
        return ProductCard(
            view=self._view,
            expect=self._expect,
            selector=(self.S_PRODUCT_CARD + self.S_CARD_ADDITION_TEMPLATE).format(index=index),
        )

    def get_all_products_cards(self) -> list[ProductCard]:
        return [
            self.get_product_card_by_index(index) for index in range(1, self.get_products_cards_count() + 1)
        ]

    def open_main_menu(self) -> MainMenuItems:
        return self._main_menu.open()

    def verify_lbl_shop_name_text(self, expected_shop_name: str) -> None:
        self.__lbl_shop_name.verify_is_visible()
        lbl_text = self.__lbl_shop_name.get_text()
        assert lbl_text == expected_shop_name
