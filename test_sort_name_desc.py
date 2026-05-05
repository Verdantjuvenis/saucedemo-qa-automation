from pages.inventory_page import InventoryPage


def test_sort_name_z_to_a(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.select_sort_za()

    names = inventory_page.get_item_names()

    assert names == sorted(names, reverse=True)