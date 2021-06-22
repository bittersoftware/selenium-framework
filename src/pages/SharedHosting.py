from framework.src.pages.locators.SharedHostingLocator import (
    SharedHostingLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url
import logging as logger


class SharedHosting(SharedHostingLocator):
    endpoint = "/shared-hosting"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_shared_hosting(self):
        base_url = get_base_url()
        self.driver.get(base_url + self.endpoint)
        logger.info(f"Going to {self.endpoint}")

    def get_page_title_h1_text(self):
        return self.sl.wait_and_get_text(self.TITLE_H1)
