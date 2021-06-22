from selenium.webdriver.common.by import By


class HomePageLocator:

    COOKIE_BTN = (By.CSS_SELECTOR, "a.cookie-accept")
    GET_STARTED = (By.CSS_SELECTOR, "div > a.cta-hero-home")

    # Nav Menu
    WEB_HOSTING = (By.ID, "webHostingDropDown")
    # Sub-Menu
    SHARED_HOSTING = (By.CSS_SELECTOR, "a[title='Shared Hosting']")

    # Compare Plans options
    WORDPRESS_HOSTING = (By.CSS_SELECTOR, "div.imh-wp")
