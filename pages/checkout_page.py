from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
        ).send_keys(postal_code)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_success_message_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text