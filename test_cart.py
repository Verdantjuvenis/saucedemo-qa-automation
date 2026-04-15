import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_add_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_text() == "1"


def test_remove_item_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    logged_in_driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    badges = logged_in_driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0