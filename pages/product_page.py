from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_in_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
        self.solve_quiz_and_get_code()
        self.should_be_right_item()
        self.should_be_right_price()

    def should_be_right_item(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        appeared_product_name = self.browser.find_element(*ProductPageLocators.APPEARED_PRODUCT_NAME).text
        assert str(product_name) == str(appeared_product_name), 'Product name should be equal chosen product name'

    def should_be_right_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        appeared_price = self.browser.find_element(*ProductPageLocators.APPEARED_PRICE).text
        assert str(price) == str(appeared_price), 'Price should be equal chosen product price'
