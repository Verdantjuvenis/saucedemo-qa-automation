from selenium.webdriver.common.by import By


class InventoryPage:
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        return self.driver.find_elements(*self.INVENTORY_ITEMS)

    def get_title_text(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()

    def get_cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()