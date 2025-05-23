from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert-success')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BASKET = (By.CSS_SELECTOR, 'span a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    HELP_ICON = (By.CSS_SELECTOR, '[data-analytics-id="HELP_AND_DOCS_OPENED"]')

class BasketPageLocators:
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, '#basket_formset')

class NewLoginPageLocators:
    USE_EMAIL_BUTTON = (By.CSS_SELECTOR, '[data-ui-role="use-email"]')
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.SKKcm')

