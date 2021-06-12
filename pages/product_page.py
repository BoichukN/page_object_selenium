from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BTN)
        add_link.click()

    def should_be_see_message_product_add(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "No successful message"

    def should_be_name_product_in_message_the_same_as_added(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text

        assert name_in_message == name_product, 'Product name in messages not valid'

    def should_be_price_in_basket_be_equal_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert price_in_message == price_product, 'Price in basket not valid'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_messages_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear in 4sec"
