from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRODUCT_LIST = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REP_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, "[class ='alertinner '] > p strong")
    SUCCESS_PRODUCT_NAME = (By.XPATH, "(//div[@class ='alertinner ']/strong)[1]")




