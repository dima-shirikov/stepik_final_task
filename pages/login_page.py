from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login отсутствует в ссылке'

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.FORM_LOGIN)
        assert True, 'Форма логина отсутствует на странице'

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.FORM_REGISTRY)
        assert True, 'Форма регистрации отсутствует на странице'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.MAIL_REGISTRY).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRY).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_VALID_REGISTRY).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRY).click()
