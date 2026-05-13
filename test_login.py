import csv
import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_pass")

    assert "epic sadface" in login_page.get_error_text().lower()


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_text().lower()

login_test_data = []

with open("login_data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        login_test_data.append(
            (
                row["username"],
                row["password"],
                row["expected_result"]
            )
        )

@pytest.mark.parametrize(
    "username,password,expected_result",
    login_test_data
)
def test_login_scenarios(driver, username, password, expected_result):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    if expected_result == "success":
        assert "inventory" in driver.current_url

    elif expected_result == "locked":
        assert "locked out" in login_page.get_error_text().lower()

    elif expected_result == "failure":
        assert "epic sadface" in login_page.get_error_text().lower()