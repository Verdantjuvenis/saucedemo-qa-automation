from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGES = (By.CLASS_NAME, "shopping_cart_badge")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def remove_backpack(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REMOVE_BACKPACK_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.CART_BADGES)
        )

    def get_badges(self):
        return self.driver.find_elements(*self.CART_BADGES)

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()