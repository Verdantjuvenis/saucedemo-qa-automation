import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_complete_checkout(logged_in_driver):
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    logged_in_driver.find_element(By.ID, "checkout").click()

    logged_in_driver.find_element(By.ID, "first-name").send_keys("Kev")
    logged_in_driver.find_element(By.ID, "last-name").send_keys("Test")
    logged_in_driver.find_element(By.ID, "postal-code").send_keys("12345")
    logged_in_driver.find_element(By.ID, "continue").click()
    logged_in_driver.find_element(By.ID, "finish").click()

    message = WebDriverWait(logged_in_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    assert "checkout-complete" in logged_in_driver.current_url
    assert "thank you" in message.text.lower()


def test_checkout_missing_postal_code(logged_in_driver):
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    logged_in_driver.find_element(By.ID, "checkout").click()

    logged_in_driver.find_element(By.ID, "first-name").send_keys("Kev")
    logged_in_driver.find_element(By.ID, "last-name").send_keys("Test")
    logged_in_driver.find_element(By.ID, "continue").click()

    error = logged_in_driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "postal code is required" in error.text.lower()