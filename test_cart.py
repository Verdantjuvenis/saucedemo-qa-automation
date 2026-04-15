import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_add_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_text() == "1"


def test_remove_item_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.remove_backpack()

    assert len(cart_page.get_badges()) == 0