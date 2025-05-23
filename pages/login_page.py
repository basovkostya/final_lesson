from .base_page import BasePage
from .locators import LoginPageLocators, NewLoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Не содержит подстроку "Login"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет формы для логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Нет формы для регистрации'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def new_login_user(self, email, password):
        self.browser.find_element(*NewLoginPageLocators.USE_EMAIL_BUTTON).click()
        self.browser.find_element(*NewLoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*NewLoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*NewLoginPageLocators.LOGIN_BUTTON).click()