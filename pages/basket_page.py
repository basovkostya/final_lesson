from .base_page import BasePage
from .locators import BasketPageLocators
import math

class BasketPage(BasePage):
    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "Уведомление о том, что корзина пуста не появилась"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "В корзине есть товары"


