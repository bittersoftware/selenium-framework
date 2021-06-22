from framework.src.pages.locators.HomePageLocator import (
    HomePageLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url
import logging as logger


class HomePage(HomePageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_home(self):
        base_url = get_base_url()
        self.driver.get(base_url)
        logger.info(f"Going to {base_url}")

    def click_accept_cookie(self):
        logger.info("Accepting cookies")
        self.sl.wait_and_click(self.COOKIE_BTN)

    def click_get_started_button(self):
        self.sl.wait_and_click(self.GET_STARTED)

    def click_shared_hosting(self):
        self.sl.hover_and_click(self.WEB_HOSTING, self.SHARED_HOSTING)

    def click_compare_plans_wordpress_hosting(self):
        self.sl.wait_and_click(self.WORDPRESS_HOSTING)
