from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "[name='login_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_TO_BASKET_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    ADDED_TO_BASKET_SUCCESS_MSG = (By.CSS_SELECTOR, ".alertinner")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "p strong")
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, "[href='/en-gb/basket/']")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
