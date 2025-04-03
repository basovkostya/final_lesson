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
        assert  name == self.get_name_product(), 'Название продукта не та в уведомлении'

    def message_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Уведомление о добавлении товара не появилась"

    def get_name_product(self):
        really_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = really_product_name.text
        return name

    def price_comparison(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price_basket.text == price_product.text, 'Цена не соответствует в корзине'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADD_TO_BASKET)
