from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"expected login to be in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        register_email.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        register_password.send_keys(password)
        register_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        register_confirm_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
