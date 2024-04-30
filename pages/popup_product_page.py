import allure

from locators.locators import Locators
from pages.base_page import BasePage
from pages.basket_page import BasketPage


class PopUpProductPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.timeout = timeout

    @allure.step("Go to basket page.")
    def go_to_basket_page(self):
        self.click(Locators.go_to_basket_xpath)
        return BasketPage(self.driver)

    @allure.step("Return to product page.")
    def go_to_product_page(self):
        self.click(Locators.continue_shopping_xpath)

