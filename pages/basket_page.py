import allure

from locators.locators import Locators
from pages.base_page import BasePage


class BasketPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Check amount in basket.")
    def check_amount_of_basket(self):
        amount_of_basket_element = self.find(Locators.amount_of_basket)
        price_of_item = amount_of_basket_element.text
        price_of_item_with_dot = price_of_item.replace(',', '.')
        cleaned_amount = ''.join(char for char in price_of_item_with_dot if char.isdigit() or char in {',', '.'})
        amount_of_basket = float(cleaned_amount.replace(',', '.'))
        return amount_of_basket

