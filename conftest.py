from dotenv import load_dotenv
import os
import pytest
load_dotenv()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against: chrome or brave"
    )

    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against: qa or staging"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)

    elif browser == "brave":
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    yield driver
    driver.quit()

@pytest.fixture
def base_url(request):
    env = request.config.getoption("--env")

    urls = {
        "qa": os.getenv("BASE_URL", "https://www.saucedemo.com/"),
        "staging": "https://www.saucedemo.com/",
    }

    if env not in urls:
        raise ValueError(f"Unsupported environment: {env}")

    return urls[env]

@pytest.fixture
def logged_in_driver(driver, base_url):
    login_page = LoginPage(driver)
    login_page.login(
        os.getenv("STANDARD_USER"),
        os.getenv("STANDARD_PASSWORD"),
        base_url
    )
    return driver

import requests


@pytest.fixture
def users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    return response.json()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)