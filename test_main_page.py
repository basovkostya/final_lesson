import time
import pytest

from pages.locators import NewLoginPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


@pytest.mark.login_quest
class TestLoginFromPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.skip
def test_login_register_form(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_with_header_basket()
    page.basket_is_empty()
    page.message_basket_is_empty()

def test_new_login_page(browser):
    link = 'https://my.audit.webmonitorx.ru/login'
    page = LoginPage(browser, link)
    page.open()
    page.new_login_user('kbasov@webmonitorx.ru', 'Kultivator4!')
    page.should_be_authorized_user()

