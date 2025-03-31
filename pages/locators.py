from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTRY = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    NAME_BOOK = (By.CSS_SELECTOR, '[class = "col-sm-6 product_main"] h1')
    CHECK_NAME_BOOK = (By.CSS_SELECTOR, '#messages .alert-success:nth-of-type(1) strong')
    PRICE_BOOK = (By.CSS_SELECTOR, '[class = "col-sm-6 product_main"] p:nth-of-type(1)')
    CHECK_PRICE_BOOK = (By.CSS_SELECTOR, '#messages .alert-info p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-of-type(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, "span[class = btn-group]>a")


class BasketPageLocators():
    IS_TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    IS_PRODUCT = (By.CSS_SELECTOR, ".basket-items")