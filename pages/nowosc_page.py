from time import sleep
import allure
from locators.locators import Locators
from pages.base_page import BasePage
from pages.product_page import ProductPage


class NowoscPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on first product on the page.")
    @allure.step("Verify if picture displays correctly.")
    def click_on_first_item(self):
        image_element = self.find(Locators.picture_img_xpath)
        image_attribute = image_element.get_attribute("alt")
        self.click(Locators.picture_xpath)
        return image_attribute

    @allure.step("Click on {number_of_item} product on the page.")
    def click_on_nth_item(self, number_of_item):
        image_element = f"//section/div[{number_of_item}]/a/picture"
        sleep(3)
        self.click(image_element)
        return ProductPage(self.driver)
