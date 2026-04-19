from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import Select


def test_sort_price_high_to_low(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)

    # Select dropdown
    dropdown = driver.find_element(*inventory_page.SORT_DROPDOWN)
    select = Select(dropdown)
    select.select_by_visible_text("Price (high to low)")

    # Get prices
    prices = inventory_page.get_item_prices()

    # Convert "$29.99" → 29.99
    prices = [float(price.replace("$", "")) for price in prices]

    # Check descending order
    assert prices == sorted(prices, reverse=True)