import allure
from locators.locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_warning_message(self):
        return self.get_text(Locators.warning_message_xpath)

    @allure.step("Login to application")
    def log_into_application(self, username,password):
        self.set(Locators.username_textbox_xpath, username)
        self.set(Locators.password_textbox_xpath, password)
        self.click(Locators.login_button_xpath)

    @allure.step("Successful Login Confirmation - adjusting the name to reflect successful login with correct data and unsuccessful login with incorrect data")
    def verify_logged_succesfully(self):
        """
        If name 'uwaga' (method return True) visible on page, then user is not logged succesfully
        """
        return self.is_element_visible(Locators.uwaga_xpath)

