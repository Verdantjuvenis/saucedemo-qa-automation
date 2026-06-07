import os
import csv
from pathlib import Path
import pytest
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login(driver, base_url):
    login_page = LoginPage(driver)
    login_page.login(
        os.getenv("STANDARD_USER"),
        os.getenv("STANDARD_PASSWORD"),
        base_url
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver, base_url):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_pass", base_url)

    assert "epic sadface" in login_page.get_error_text().lower()


def test_locked_out_user(driver, base_url):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce", base_url)

    assert "locked out" in login_page.get_error_text().lower()

login_test_data = []

from pathlib import Path

LOGIN_DATA = Path(__file__).parent / "login_data.csv"

with open(LOGIN_DATA, newline="") as csvfile:
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

def test_login_scenarios(driver, base_url, username, password, expected_result):
    driver.get(os.getenv("BASE_URL"))

    login_page = LoginPage(driver)

    login_page.login(username, password, base_url)

    if expected_result == "success":
        assert "inventory" in driver.current_url

    elif expected_result == "locked":
        assert "locked out" in login_page.get_error_text().lower()

    elif expected_result == "failure":
        assert "epic sadface" in login_page.get_error_text().lower()