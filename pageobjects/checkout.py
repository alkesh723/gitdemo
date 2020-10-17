from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, dt):
        self.dt = dt
        checkouts = (By.xpath, "//div[@class='checkbox checkbox-primary']")
        done = (By.CSS_SELECTOR, "input[class*='btn-success']")

    def checkit(self):

        return self.dt.find_element(*CheckOut.checkouts)

    def uceee(self):
        return self.dt.find_element(*CheckOut.done)
