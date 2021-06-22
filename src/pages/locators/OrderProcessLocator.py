from selenium.webdriver.common.by import By


class OrderProcessLocator:

    CART_ICON = (By.CLASS_NAME, "cart-icon")
    CONTINUE_BTN = (By.ID, "sidebar-next-step")
    TOTAL = (By.CSS_SELECTOR, "div.sidebar-total h3")
    EMPTY_CART = (By.CLASS_NAME, "empty-cart")
