import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.GetStartedPage import GetStartedPage


@pytest.mark.usefixtures("init_driver")
class TestTwoYearProducts:
    @pytest.mark.tcid2
    def test_two_year_product_price_and_name(self):
        home = HomePage(self.driver)
        get_started = GetStartedPage(self.driver)

        get_started_url = (
            "https://www.inmotionhosting.com/shared-hosting#business-shared-rostrum"
        )

        duration_target = "2 Year"

        product_1_name = "Launch"
        product_2_name = "Power"
        product_3_name = "Pro"

        product_1_price = "$5.99/mo"
        product_2_price = "$5.99/mo"
        product_3_price = "$14.99/mo"

        # 1. Go to my account
        home.go_to_home()

        # 2. Type username
        home.click_get_started_button()

        # 3. Get page url
        assert (
            self.driver.current_url == get_started_url
        ), f"Expected url: {get_started_url}"

        # 4. Wait for "Launch" product to be displayed
        duration_list = get_started.wait_and_get_duration_list()

        # 5. Confirm 2 Year option is present and selected
        btn_2y = duration_list[0]
        assert btn_2y.text == duration_target, f"Expected {duration_target}"
        assert "uk-active" in btn_2y.get_attribute("class"), "Expected class: uk-active "

        # 6. Assert name and price is correct for each product
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
