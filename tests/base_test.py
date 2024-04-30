import unittest
import allure
from selenium import webdriver
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.nowosc_page import NowoscPage
from pages.popup_product_page import PopUpProductPage
from pages.product_page import ProductPage
from allure_commons.types import AttachmentType


class BaseTest(unittest.TestCase, BasePage):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self._outcome = None

    @allure.step("Open ertom.eu website.")
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.basePage = BasePage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.nowosciPage = NowoscPage(self.driver)
        self.productPage = ProductPage(self.driver)
        self.popupProductPage = PopUpProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
    @allure.step("Close ertom.eu website.")
    def tearDown(self):
        if self._outcome.errors:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.driver.close()
        self.driver.quit()


