import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_add_item_to_cart(logged_in_driver):
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"


def test_remove_item_from_cart(logged_in_driver):
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in_driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    badges = logged_in_driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0