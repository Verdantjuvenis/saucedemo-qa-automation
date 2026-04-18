from pages.inventory_page import InventoryPage


def test_sort_items_az(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.select_sort_az()
    item_names = inventory_page.get_item_names()

    assert item_names == sorted(item_names)