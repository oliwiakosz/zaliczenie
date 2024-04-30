import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout


    def find(self, locator):
        if not isinstance(locator, str):
            raise ValueError("Locator must be a string.")
        if locator.startswith("//") or locator.startswith(".//"):
            # Jeśli locator zaczyna się od "//" lub ".//", zakładamy, że to pełny XPath
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        elif locator.endswith("_xpath"):
            # Jeśli locator kończy się na "_xpath", używamy getattr
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, getattr(Locators, locator)))
            )

        elif locator.endswith("_id"):
            # Jeśli locator kończy się na "_id", używamy getattr
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.ID, getattr(Locators, locator)))
            )
        elif locator.isalpha():
            # Jeśli locator składa się tylko z liter, spróbuj znaleźć element po ID
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.ID, locator))
                    #     presence_of_element_located
                )
            except:
                raise ValueError(f"Element with id='{locator}' not found.")
        else:
            raise ValueError(f"Unsupported locator format: {locator}")

    @allure.step("Click on field {locator}")
    def click(self, locator):
        element = self.find(locator)
        element.click()

    @allure.step("Enter the value {value} in field {locator}")
    def set(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    @allure.step("Extract text form the field {locator}")
    def get_text(self, locator):
        return self.find(locator).text


    def get_title(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        ).get_attribute("textContent")

    @allure.step("Verify page with title {page_name}")
    def verify_page(self, page_name):
        return "//div[@id='menu_navbar']//a[@title='" + page_name + "']"

    @allure.step("Click popup")
    def click_popup(self, locator):
        popup_locator = (By.ID, "ck_dsclr_v2")
        wait = WebDriverWait(self.driver, self.timeout)
        popup = wait.until(EC.presence_of_element_located(popup_locator))
        return popup

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def is_element_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def allure_body_description(self, jiraId, testName):
        description_text = f"{jiraId} - {testName}"
        allure.dynamic.title(description_text)
