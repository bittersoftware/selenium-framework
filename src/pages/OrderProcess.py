from framework.src.pages.locators.OrderProcessLocator import (
    OrderProcessLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url
import logging as logger


class OrderProcess(OrderProcessLocator):
    endpoint = "/order-process#hosting"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_order_process(self):
        base_url = get_base_url()
        self.driver.get(base_url + self.endpoint)
        logger.info(f"Going to {self.endpoint}")

    def wait_cart_icon(self):
        self.sl.wait_visibility_of_element(self.CART_ICON, timeout=30)

    def get_total(self):
        total = self.sl.wait_and_get_text(self.TOTAL)
        logger.info(f"Total: {total}")
        return total

    def click_empty_car(self):
        self.sl.wait_and_click(self.EMPTY_CART)
