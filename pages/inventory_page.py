from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

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

    def select_sort_az(self):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("Name (A to Z)")

    def get_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]
    
    def get_item_prices(self):
        items = self.driver.find_elements(*self.ITEM_PRICES)
        return [item.text for item in items]
    
    def select_sort_price_high_to_low(self):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("Price (high to low)")