from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BTN)
        add_link.click()

    def should_be_see_message_product_add(self):
        self.should_be_price_in_basket_be_equal_price_product()
        self.should_be_name_product_in_message_the_same_as_added()

    def should_be_name_product_in_message_the_same_as_added(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text

        assert name_in_message == name_product, 'Product name in messages not valid'

    def should_be_price_in_basket_be_equal_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text

        assert price_in_message == price_product, 'Price in basket not valid'
