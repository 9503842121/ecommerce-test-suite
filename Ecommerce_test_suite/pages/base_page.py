from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, by, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return None

    def click(self, by, locator):
        element = self.wait_for_element(by, locator)
        if element:
            element.click()

    def send_keys(self, by, locator, value):
        element = self.wait_for_element(by, locator)
        if element:
            element.send_keys(value)
