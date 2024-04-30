import re
from time import sleep

import allure

from locators.locators import Locators
from pages.base_page import BasePage
from pages.popup_product_page import PopUpProductPage


class ProductPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.timeout = timeout


    def number_of_pieces_available(self):
        sleep(5)
        numberString = self.get_text(Locators.number_of_pieces_xpath)
        extracted_number = None
        matches = re.findall(r'\d+', numberString)
        if matches:
            extracted_number = int(matches[0])
        else:
            print("Brak liczby w tekście.")
        return extracted_number

    @allure.step("Select number of product.")
    def select_number_of_products(self, number_of_items):
        single_item_price = self.check_price_of_item()
        amount_of_items = single_item_price * number_of_items
        sleep(2)
        self.click(Locators.list_of_items_xpath)
        if number_of_items <= 5:
            number_of_items_xpath = "//a[@data-value='" + str(number_of_items) + "']"
            self.click(number_of_items_xpath)
        else:
            number_of_items_xpath = "//a[@data-value='null']"
            self.click(number_of_items_xpath)
            self.set(Locators.list_of_items_input_xpath, number_of_items)
        sleep(5)
        return amount_of_items

    @allure.step("Add item to basket.")
    def add_items_to_basket(self):
        self.click(Locators.add_to_basket)
        return PopUpProductPage(self.driver)

    @allure.step("Checking price of item.")
    def check_price_of_item(self):
        price_of_item = self.get_text(Locators.projektor_price_value_xpath)
        price_of_item_with_dot = price_of_item.replace(',', '.')
        extracted_number = round(float(price_of_item_with_dot[:-2]), 2)
        return extracted_number






