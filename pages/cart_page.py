from selenium.webdriver.common.by import By


class CartPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGES = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.find_element(*self.CART_LINK).click()

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK_BUTTON).click()

    def get_badges(self):
        return self.driver.find_elements(*self.CART_BADGES)