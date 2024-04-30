from time import sleep
import allure
from locators.locators import Locators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.nowosc_page import NowoscPage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on login icon")
    def click_login_icon(self):
        self.click(Locators.accept_message_xpath)
        self.click(Locators.login_icon_xpath)
        return LoginPage(self.driver)

    @allure.step("Click on basket icon")
    def click_basket(self):
        self.click(Locators.basket_icon_xpath)

    @allure.step("Click on nowosci")
    def click_nowosci(self):
        sleep(3)
        self.click(Locators.nowosci_xpath)
        return NowoscPage(self.driver)
