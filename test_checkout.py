import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_complete_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("Kev", "Test", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    message = checkout_page.get_success_message_element()
    assert "checkout-complete" in logged_in_driver.current_url
    assert "thank you" in message.text.lower()


def test_checkout_missing_postal_code(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    checkout_page.start_checkout()
    checkout_page.enter_first_name("Kev")
    checkout_page.enter_last_name("Test")
    checkout_page.continue_checkout()

    assert "postal code is required" in checkout_page.get_error_text().lower()