from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_add_page(self):
        self.should_be_promo_link()
        self.should_be_add_to_basket_btn()

    def should_be_promo_link(self):
        assert 'promo' in self.browser.current_url, f"expected promo to be in {self.browser.current_url}"

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "add to basket button is not presented"

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_added_to_basket(self):
        find_product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_PRODUCT).text
        product_in_the_basket = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT).text
        added_to_basket_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MSG).text
        full_message = f"{product_in_the_basket} {added_to_basket_message}"
        assert f"{find_product_name} has been added to your basket" in full_message, \
            f"expected {find_product_name} has been added to your basket"

    def price_should_be_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        price_on_product_page = self.browser.find_element(*ProductPageLocators.PRICE_ON_PRODUCT_PAGE).text
        assert basket_price == price_on_product_page, \
            f"expected basket price: {basket_price} be equal to the price on product page: {price_on_product_page}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_SUCCESS_MSG), \
            "Success message should disappear, but it does not"





