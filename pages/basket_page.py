from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.IS_PRODUCT), "В корзине есть товары"

    def check_is_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.IS_TEXT_BASKET_EMPTY), "Отсутствует текст о том, что корзина пустая"


