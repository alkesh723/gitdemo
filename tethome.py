from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TetHome:
    def subi(self):
        dt = webdriver.Firefox(executable_path="C:\\Users\Alkesh\Desktop\PALAKH\geckodriver.exe")
        dt.implicitly_wait(5)

        dt.get("https://rahulshettyacademy.com/angularpractice/")
        dt.find_element_by_css_selector("a[href*='shop']").click()

        black = dt.find_elements_by_xpath("//div[@class='card h-100']")

        for jt in black:
            pro = jt.find_element_by_xpath("div/h4/a").text
            if pro == "Blackberry":
                jt.find_element_by_xpath("div/button").click()
        dt.find_element_by_css_selector("a[class*='btn-primary']").click()
        dt.find_element_by_css_selector("button[class*='btn-success']").click()
        dt.find_element_by_xpath("//input[@id='country']").send_keys("ind")
        wait = WebDriverWait(dt, 6)

        dt.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        dt.find_element_by_css_selector("input[class*='btn-success']").click()
        suc = dt.find_element_by_css_selector(".alert-success").text
