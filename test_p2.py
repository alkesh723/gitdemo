from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest


from baseclass.base import BaseClass
from pageobjects.checkout import CheckOut
from pageobjects.homepage import HomePage

@pytest.mark.usefixtures("test_set")
class FamEz(BaseClass):

    def test_p(self, test_set):
        homepage = HomePage(self.dt)
        homepage.shoitem().click
        self.dt.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.dt.find_element_by_css_selector("button[class*='btn-success']").click()
        self.dt.find_element_by_xpath("//input[@id='country']").send_keys("ind")
        wait = WebDriverWait(self.dt, 6)

        check = CheckOut(self.dt)
        check.checkit().click
        self.dt.find_element_by_css_selector("input[class*='btn-success']").click()
        suc = self.dt.find_element_by_css_selector(".alert-success").text
        assert "Success! Thank you!" in suc
