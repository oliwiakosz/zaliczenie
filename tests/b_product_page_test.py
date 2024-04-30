import unittest
from time import sleep
import allure
import pytest
from tests.base_test import BaseTest
from utils.cookies import saveCookies, loadCookies
from utils.test_data import TestData



@pytest.mark.smoke_test
class ProductPageTest(BaseTest):

    @allure.description("This test verifies product page.")
    def test_104_check_picture_of_product(self):
        self.allure_body_description(104, "Verify product image ")
        self.driver.get(TestData.url)
        self.homePage.click_login_icon()
        self.loginPage.log_into_application(TestData.email, TestData.password)
        self.driver.get(TestData.url)

        image_attribute = self.homePage.click_nowosci().click_on_first_item()
        text_title = self.basePage.get_title()
        saveCookies(self.driver)
        self.assertIn(image_attribute, text_title)


    @allure.description("This test verifies the product price.")
    @pytest.mark.smoke_test
    def test_105_check_product_price(self):
        self.allure_body_description(105, "Verify the product price")
        self.driver.get(TestData.url)
        loadCookies(self.driver)
        sleep(4)
        actual_price = self.productPage.check_price_of_item()
        expected_price = 30.69
        assert expected_price == actual_price

    @allure.description("This test checks whether the product is available")
    def test_106_check_number_of_available_items(self):
        self.allure_body_description(106, "Verify number of available items")
        self.driver.get(TestData.url)
        loadCookies(self.driver)
        number_of_product = self.productPage.number_of_pieces_available()
        assert number_of_product > 0


if __name__ == '__main__':
    unittest.main()
