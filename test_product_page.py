from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{num}" for num in range(10)]


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, login_link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, login_link)
        page.open()
        page.go_to_login_page()


@pytest.mark.need_review
#@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_be_promo_add_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket()
    page.price_should_be_basket_price()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, product_base_link)
    page.open()
    page.view_basket()
    page.should_be_no_products_in_the_basket()
    page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "PraiseTheSun!"
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.add_to_basket()
        page.should_be_added_to_basket()
        page.price_should_be_basket_price()





