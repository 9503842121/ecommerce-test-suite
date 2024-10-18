from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_LINK = (By.ID, "nav-cart")
    QUANTITY_DROPDOWN = (By.NAME, "quantity")
    DELETE_BUTTON = (By.XPATH, "//input[@value='Delete']")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def update_quantity(self, quantity):
        self.click(*self.CART_LINK)
        quantity_dropdown = self.wait_for_element(*self.QUANTITY_DROPDOWN)
        quantity_dropdown.send_keys(quantity)

    def remove_from_cart(self):
        self.click(*self.CART_LINK)
        self.click(*self.DELETE_BUTTON)

    def get_cart_count(self):
        return int(self.wait_for_element(*self.CART_COUNT).text)
