from selenium.webdriver.common.by import By


class WordPressHostingLocator:

    CLOSE_MODAL = (By.CSS_SELECTOR, "button.modal-close-btn")
    TITLE_H1 = (By.TAG_NAME, "h1")
    SAVE_NOW = (By.CSS_SELECTOR, "div.business-rostrum-card.most-popular-card button")
    ADD_TO_CART_LIST = (By.CSS_SELECTOR, "div.business-rostrum-card button")
