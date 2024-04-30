from ddt import file_data, ddt, data, unpack
from base_test import BaseTest
from utils.cookies import saveCookies
from utils.test_data import TestData
@ddt
class LoginTest(BaseTest):

    @file_data("../testdata/testdata.json")
    @unpack
    def test_check_valid_and_invalid_credentials(self, jiraId, testName, username, password, correctData):

        self.allure_body_description(jiraId, testName)
        self.driver.get(TestData.url)
        self.homePage.click_login_icon()
        self.loginPage.log_into_application(username, password)

        is_visible = self.loginPage.verify_logged_succesfully()
        if correctData == 'Y':
            saveCookies(self.driver, save_path='testdata')
            assert is_visible == False
            actual_title = self.loginPage.get_title()
            expected_title = "Fotoramki, fotoalbumy, albumy ślubne - Ertom. Hurtownia fotograficzna"
            assert actual_title == expected_title

        else:
            assert is_visible == True
            actual_message = self.loginPage.get_warning_message()
            expected_message = "Podany login lub hasło nie jest poprawne."
            assert actual_message == expected_message
