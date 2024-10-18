import pytest
from selenium import webdriver
from pages.search_page import SearchPage
from pages.cart_page import CartPage
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()


def test_search_non_existing_product(setup):
    search_page = SearchPage(setup)
    search_page.search_product("ld345tsxslfer")
    assert search_page.no_results_found(), "No results found message not displayed"


def test_search_existing_product(setup):
    search_page = SearchPage(setup)
    search_page.search_product("Laptop")
    search_page.select_product()
    assert "Laptop" in setup.title, "Product page title does not contain 'Laptop'"


def test_add_to_cart(setup):
    search_page = SearchPage(setup)
    cart_page = CartPage(setup)

    search_page.search_product("Laptop")
    search_page.select_product()

    cart_page.add_to_cart()
    assert cart_page.get_cart_count() == 1, "Cart count is not 1 after adding the product"


def test_update_cart_quantity(setup):
    search_page = SearchPage(setup)
    cart_page = CartPage(setup)

    search_page.search_product("Laptop")
    search_page.select_product()

    cart_page.add_to_cart()
    cart_page.update_quantity("2")
    assert cart_page.get_cart_count() == 2, "Cart count did not update to 2"


def test_remove_from_cart(setup):
    search_page = SearchPage(setup)
    cart_page = CartPage(setup)

    search_page.search_product("Laptop")
    search_page.select_product()

    cart_page.add_to_cart()
    cart_page.remove_from_cart()
    assert cart_page.get_cart_count() == 0, "Cart is not empty after removing the product"
