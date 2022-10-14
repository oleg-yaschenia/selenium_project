from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/",\
            "Login URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            "Register form is not presented"

    def register_new_user(self, email, password1, password2):
        self.is_element_to_use(*LoginPageLocators.REG_LOGIN_FIELD).send_keys(email)
        self.is_element_to_use(*LoginPageLocators.REG_PASSWORD_FIELD).send_keys(password1)
        self.is_element_to_use(*LoginPageLocators.REG_REP_PASSWORD_FIELD).send_keys(password2)
        self.is_element_to_use(*LoginPageLocators.REGISTER_BUTTON).click()

