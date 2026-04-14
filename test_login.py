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