from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text