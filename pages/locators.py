from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span//a[contains(@href, 'basket')]")


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    APPEARED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1) strong')
    APPEARED_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CLASS_NAME, 'basket-title')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner> p a')

