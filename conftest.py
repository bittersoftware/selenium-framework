import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
import os


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ["chrome", "ch", "headlesschrome", "firefox", "ff"]
    browser = os.environ.get("BROWSER", None)
    if not browser:
        raise EnvironmentError("The environment variable BROWSER must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise EnvironmentError("Provide supported browser")

    if browser in ("chrome", "ch"):
        chrome_options = ChOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ("firefox", "ff"):
        driver = webdriver.Firefox()
    elif browser in ("headlesschrome"):
        chrome_options = ChOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver
    yield
    driver.quit()
