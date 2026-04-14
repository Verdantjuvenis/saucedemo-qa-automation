import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_inventory_items_display(logged_in_driver):
    items = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0


def test_inventory_page_title(logged_in_driver):
    title = logged_in_driver.find_element(By.CLASS_NAME, "title")
    assert "products" in title.text.lower()