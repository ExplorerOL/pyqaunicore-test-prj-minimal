from pyqaunicore.ui.primitives import Button, Container
from pyqaunicore.ui.primitives.image import Image
from pyqaunicore.ui.primitives.label import Label

from support.loggers.testrun_logger import logger


class ProductCard(Container):
    S_BTN_ADD_TO_CART = '[class="pricebar"]:button'
    S_LBL_PRICE = '[data-test="inventory-item-price"]'
    S_LBL_ITEM_NAME = '[data-test="inventory-item-name"]'
    S_LBL_ITEM_DESC = '[data-test="inventory-item-desc"]'
    S_IMG_ITEM = '[class="inventory_item_img"]'

    def __init__(
        self,
        page,
        expect,
        selector,
        text: str | None = None,
        name_in_log: str | None = None,
    ):
        logger.deep_trace('ProductCard.__init__')
        super().__init__(
            page=page,
            expect=expect,
            selector=selector,
            text=text,
            name_in_log=name_in_log,
        )

        self._btn_add_to_cart = Button(
            page=page,
            expect=expect,
            selector=self.S_BTN_ADD_TO_CART,
            name_in_log='Кнопка добавления в корзину',
        )
        self._lbl_price = Label(
            page=page,
            expect=expect,
            selector=f'{self._selector} {self.S_LBL_PRICE}',
            name_in_log='Надпись цена',
        )
        self._lbl_name = Label(
            page=page,
            expect=expect,
            selector=f'{self._selector} {self.S_LBL_ITEM_NAME}',
            name_in_log='Надпись названия товара',
        )
        self._lbl_desc = Label(
            page=page,
            expect=expect,
            selector=f'{self._selector} {self.S_LBL_ITEM_DESC}',
            name_in_log='Надпись описания товара',
        )
        self._img_item = Image(
            page=page,
            expect=expect,
            selector=self.S_IMG_ITEM,
            name_in_log='Картинка товара',
        )

    def get_product_name(self) -> str | None:
        return self._lbl_name.get_text()

    def verify_product_name(self, expected_name: str):
        self._lbl_name.verify_has_text(expected_text=expected_name)

    def verify_product_price(self, expected_price: str):
        self._lbl_price.verify_has_text(expected_text=expected_price)

    def verify_product_desc(self, expected_desc: str):
        self._lbl_desc.verify_has_text(expected_text=expected_desc)
