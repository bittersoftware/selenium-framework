import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.WordPressHosting import WordPressHosting


@pytest.mark.usefixtures("init_driver")
class TestOpenComparePlans:
    @pytest.mark.tcid5
    def test_open_compare_plans_wordpress(self):
        home = HomePage(self.driver)
        wp_hosting = WordPressHosting(self.driver)

        target_url = "https://www.inmotionhosting.com/wordpress-hosting"
        expected_h1 = "WordPress Hosting"

        # 1. Go to my account
        home.go_to_home()

        # 2. Selecct Compare Plans section > WordPress Hosting
        home.click_compare_plans_wordpress_hosting()

        # 3. Assert url
        assert (
            self.driver.current_url == target_url
        ), f"Expected url: {target_url}"

        # 4. Assert page
        assert wp_hosting.get_page_title_h1_text() == expected_h1, f"Expected {expected_h1}"
