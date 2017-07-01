# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class cas2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_cas2(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, login="380961451058", password="MK2prod_2016")
        self.hello_mk(wd)
        self.assertTrue(success)

    def hello_mk(self, wd):
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()

    def login(self, wd, login, password):
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(login)
        wd.find_element_by_css_selector("button.btn.btn-default").click()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").send_keys(password)
        wd.find_element_by_xpath("//section[@id='section-left']/section[2]/div/div[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-default").click()

    def open_home_page(self, wd):
        wd.get("https://new.kyivstar.ua/ecare/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()