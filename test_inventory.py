import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_inventory_items_display(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    items = inventory_page.get_items()
    assert len(items) > 0


def test_inventory_page_title(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    assert "products" in inventory_page.get_title_text().lower()