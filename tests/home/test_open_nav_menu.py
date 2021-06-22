import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.SharedHosting import SharedHosting


@pytest.mark.usefixtures("init_driver")
class TestOpenNavMenu:
    @pytest.mark.tcid4
    def test_open_share_hosting(self):
        home = HomePage(self.driver)
        shared_hosting = SharedHosting(self.driver)

        target_url = "https://www.inmotionhosting.com/shared-hosting"
        expected_h1 = "Shared Hosting"

        # 1. Go to my account
        home.go_to_home()

        # 2. Selecct Web Hosting > Shared Hosting
        home.click_shared_hosting()

        # 3. Assert url
        assert (
            self.driver.current_url == target_url
        ), f"Expected url: {target_url}"

        # 4. Assert page
        assert shared_hosting.get_page_title_h1_text() == expected_h1, f"Expected {expected_h1}"
