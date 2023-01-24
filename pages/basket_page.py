from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def view_basket(self):
        view_basket_btn = self.browser.find_element(*BasketPageLocators.VIEW_BASKET_BTN)
        view_basket_btn.click()

    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
        assert "Your basket is empty." in empty_basket_message, "expected empty basket message"

    def should_be_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
        "Products are presented in the basket, but they should not be"