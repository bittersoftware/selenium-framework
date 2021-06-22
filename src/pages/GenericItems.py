from framework.src.pages.locators.GenericItemsLocator import (
    GenericItemsLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
import logging as logger


class GenericItems(GenericItemsLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def click_close_modal(self):
        logger.info("Closing Modal")
        self.sl.wait_and_click(self.CLOSE_MODAL)

    def click_accept_cookie(self):
        logger.info("Accepting cookies")
        self.sl.wait_and_click(self.COOKIE_BTN)
