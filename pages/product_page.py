from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_CART)
        )
        element.click()
        self.solve_quiz_and_get_code()

    def check_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text

        check_name_book = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.CHECK_NAME_BOOK)  # Используем visibility
        ).text

        assert name_book == check_name_book, (
            f'Название добавленной книги не соответствует: {name_book} != {check_name_book}'
        )

    def check_price_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text

        check_price_book = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.CHECK_PRICE_BOOK)  # Используем visibility
        ).text

        assert price_book == check_price_book, (
            f'Цена добавленной книги не соответствует: {price_book} != {check_price_book}'
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"



