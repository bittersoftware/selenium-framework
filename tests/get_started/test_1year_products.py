import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.GetStartedPage import GetStartedPage
from framework.src.SeleniumExtended import SeleniumExtended


@pytest.mark.usefixtures("init_driver")
class TestOneYearProducts:
    @pytest.mark.tcid3
    def test_one_year_product_price_and_name(self):
        home = HomePage(self.driver)
        get_started = GetStartedPage(self.driver)
        sl = SeleniumExtended(self.driver)

        get_started_url = (
            "https://www.inmotionhosting.com/shared-hosting#business-shared-rostrum"
        )

        duration_target = "1 Year"

        product_1_name = "Launch"
        product_2_name = "Power"
        product_3_name = "Pro"

        product_1_price = "$6.99/mo"
        product_2_price = "$6.99/mo"
        product_3_price = "$15.99/mo"

        # 1. Go to my account
        home.go_to_home()
        home.click_accept_cookie()

        # 2. Type username
        home.click_get_started_button()

        # 3. Get page url
        assert (
            self.driver.current_url == get_started_url
        ), f"Expected url: {get_started_url}"

        # 5. Select 1 Year option
        sl.scroll_to_top()
        btn_1y = get_started.wait_and_get_duration_list()[1]
        get_started.wait_and_click_1_year_btn()

        # 6. Confirm 1 Year option is present and selected
        assert btn_1y.text == duration_target, f"Expected {duration_target}"
        assert "uk-active" in btn_1y.get_attribute("class"), "Expected class: uk-active "

        # 7. Assert name and price is correct for each product
        product_list = get_started.wait_and_get_product_list()
        price_list = get_started.wait_and_get_price_list()

        # Product names
        assert product_list[0].text == product_1_name, "Expected: {product_1_name}"
        assert product_list[1].text == product_2_name, "Expected: {product_2_name}"
        assert product_list[2].text == product_3_name, "Expected: {product_3_name}"

        # Product prices
        assert price_list[0].text == product_1_price, "Expected: {product_1_price}"
        assert price_list[1].text == product_2_price, "Expected: {product_2_price}"
        assert price_list[2].text == product_3_price, "Expected: {product_3_price}"
