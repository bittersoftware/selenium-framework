import pytest
from framework.src.pages.WordPressHosting import WordPressHosting
from framework.src.pages.GenericItems import GenericItems
from framework.src.pages.OrderProcess import OrderProcess


@pytest.mark.usefixtures("init_driver")
class TestAddToChart:
    @pytest.mark.tcid6
    def test_add_to_chart_wordpress_save_now(self):
        wp_hosting = WordPressHosting(self.driver)
        generics = GenericItems(self.driver)
        order = OrderProcess(self.driver)

        # 1. Go to my wordpress hosting
        wp_hosting.go_to_wordpress_hosting()

        # 2. Close Modal and accept cookies
        generics.click_close_modal()
        generics.click_accept_cookie()

        # 3. Add Save now to chart
        wp_hosting.add_to_cart_save_now()

        # 4. Wait for order
        order.wait_cart_icon()

        # 5. Assert total
        order.get_total()
