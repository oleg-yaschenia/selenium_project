from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert empty_basket_message == "Your basket is empty. Continue shopping", \
            f"Empty Basket message is not correct. Actual message: {empty_basket_message}"

    def empty_basket_product_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_LIST), \
            "Empty Basket contains the products"