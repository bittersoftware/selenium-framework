from framework.src.pages.locators.WordPressHostingLocator import (
    WordPressHostingLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url
import logging as logger


class WordPressHosting(WordPressHostingLocator):
    endpoint = "/wordpress-hosting"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_wordpress_hosting(self):
        base_url = get_base_url()
        self.driver.get(base_url + self.endpoint)
        logger.info(f"Going to {self.endpoint}")
        assert self.get_page_title_h1_text() == "WordPress Hosting"

    def get_page_title_h1_text(self):
        return self.sl.wait_and_get_text(self.TITLE_H1)

    def add_to_cart_save_now(self):
        el = self.sl.wait_visibility_of_element(self.SAVE_NOW)
        self.sl.move_to_element(el)
        self.sl.wait_and_click(self.SAVE_NOW)

    def click_close_modal(self):
        self.sl.wait_and_click(self.CLOSE_MODAL)
