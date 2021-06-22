from selenium.webdriver.common.by import By


class GetStartedPageLocator:

    DURATION_LIST = (By.CSS_SELECTOR, ".term-selection > li.rostrum-selector")
    LAUNCH = (By.CSS_SELECTOR, "div > h3.rostrum-heading")
    PRODUCT_LIST = (By.CSS_SELECTOR, "h3.rostrum-heading")
    PRICE_LIST = (By.CSS_SELECTOR, "div.business-price li.uk-active")
