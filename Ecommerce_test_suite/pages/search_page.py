
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    NO_RESULTS_MESSAGE = (By.XPATH, "//span[contains(text(), 'No results')]")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".s-search-results .s-title")

    def search_product(self, product_name):
        self.send_keys(*self.SEARCH_BOX, product_name)
        self.click(*self.SEARCH_BUTTON)

    def no_results_found(self):
        return self.wait_for_element(*self.NO_RESULTS_MESSAGE) is not None

    def select_product(self, index=3):
        results = self.driver.find_elements(*self.SEARCH_RESULTS)
        if len(results) > index:
            results[index].click()
