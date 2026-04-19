from pages.inventory_page import InventoryPage


def test_sort_price_high_to_low(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.select_sort_price_high_to_low()

    prices = inventory_page.get_item_prices()
    prices = [float(price.replace("$", "")) for price in prices]

    assert prices == sorted(prices, reverse=True)