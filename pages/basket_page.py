from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_see_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), "No message basket empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket has product"

    def should_not_see_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), \
            "No message basket empty, but must be"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket has product, but shouldn't"
