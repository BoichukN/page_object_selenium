from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH, "//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_PASS_CONRIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BTN = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")


class BasketPageLocators:
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-title.hidden-xs > div > h2")
