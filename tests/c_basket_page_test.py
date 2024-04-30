from time import sleep

import allure
import pytest
from tests.base_test import BaseTest
from utils.cookies import loadCookies
from utils.test_data import TestData


@pytest.mark.smoke_test
class BasketPageTest(BaseTest):

    @allure.description("This test checks the total sum of products.")
    def test_107_check_total_sum_in_basket(self):
        self.allure_body_description(107, "Verify total sum in basket.")
        self.driver.get(TestData.url)
        self.homePage.click_login_icon()
        self.driver.get(TestData.url)
        loadCookies(self.driver)
        amount_of_first_product = self.homePage.click_nowosci().click_on_nth_item(3).select_number_of_products(2)
        self.productPage.add_items_to_basket().go_to_product_page()
        sleep(5)
        amount_of_second_product = self.homePage.click_nowosci().click_on_nth_item(2).select_number_of_products(4)
        self.productPage.add_items_to_basket().go_to_product_page()
        amount_of_third_product = self.homePage.click_nowosci().click_on_nth_item(1).select_number_of_products(2)
        amount_of_first_second_third_products  =amount_of_first_product + amount_of_second_product+amount_of_third_product
        total_sum_of_basket = self.productPage.add_items_to_basket().go_to_basket_page().check_amount_of_basket()
        sleep(30)
        assert amount_of_first_second_third_products == total_sum_of_basket, "Sum of products doesn't display correctly."


