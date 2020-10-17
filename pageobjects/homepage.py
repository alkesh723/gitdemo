from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, dt):
        self.dt = dt

    shop = (By.CSS_SELECTOR, "a[href*='shop'")

    def shoitem(self):
        return self.dt.findelment(*HomePage.shop)
