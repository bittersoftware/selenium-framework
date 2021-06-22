import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.GetStartedPage import GetStartedPage


@pytest.mark.usefixtures("init_driver")
class TestGetStarted:
    @pytest.mark.tcid1
    def test_get_started(self):
        home = HomePage(self.driver)
        get_started = GetStartedPage(self.driver)

        get_started_url = (
            "https://www.inmotionhosting.com/shared-hosting#business-shared-rostrum"
        )

        # 1. Go to my account
        home.go_to_home()

        # 2. Type username
        home.click_get_started_button()

        # 3. Get page url
        assert (
            self.driver.current_url == get_started_url
        ), f"Expected url: {get_started_url}"

        # 4. Wait for "Launch" product to be displayed
        get_started.wait_for_launch_product()
