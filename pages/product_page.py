from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def product_name_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        name = product_name.text
        assert  name == self.get_name_product(), 'Продукт не добавлен'

    def message_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Товар не добавлен в корзину"

    def get_name_product(self):
        really_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = really_product_name.text
        return name