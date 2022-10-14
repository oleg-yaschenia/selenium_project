from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def clicking_on_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def comparing_product_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text
        assert product_name == added_product_name,\
            f"Added product name is not correct. " \
            f"Expected: {product_name}, " \
            f"actual: {added_product_name}"

    def comparing_product_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE).text
        assert product_price == added_product_price,\
            f"Added product price is not correct. " \
            f"Expected: {product_price}, " \
            f"actual: {added_product_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
           "Success message is presented, but should not be"




