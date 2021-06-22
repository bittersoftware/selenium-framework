from framework.src.pages.locators.GetStartedPageLocator import (
    GetStartedPageLocator,
)
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url
import logging as logger


class GetStartedPage(GetStartedPageLocator):
    endpoint = "/shared-hosting#business-shared-rostrum"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_get_started(self):
        base_url = get_base_url()
        get_started_page = base_url + self.endpoint
        self.driver.get(get_started_page)
        logger.info(f"Going to {get_started_page}")

    def wait_for_launch_product(self):
        text = self.sl.wait_and_get_text(self.LAUNCH)
        assert text == "Launch", "Expected 'Launch' product to be present"

    def wait_and_get_duration_list(self):
        elms = self.sl.wait_presence_of_all_elements_located(self.DURATION_LIST)
        logger.info(f"Duration List: {[el.text for el in elms]}")
        return elms

    def wait_and_get_product_list(self):
        elms = self.sl.wait_presence_of_all_elements_located(self.PRODUCT_LIST)
        logger.info(f"Products List: {[el.text for el in elms]}")
        return elms

    def wait_and_get_price_list(self):
        elms = self.sl.wait_presence_of_all_elements_located(self.PRICE_LIST)
        logger.info(f"Price List: {[el.text for el in elms]}")
        return elms

    def wait_and_click_2_year_btn(self):
        elms = self.wait_and_get_duration_list()
        el = elms[0]
        el.click()

    def wait_and_click_1_year_btn(self):
        elms = self.wait_and_get_duration_list()
        el = elms[1]
        el.click()

    def wait_and_click_1_month_btn(self):
        elms = self.wait_and_get_duration_list()
        el = elms[2]
        el.click()
