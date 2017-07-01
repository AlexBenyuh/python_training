# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

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
        wd.get("https://account.kyivstar.ua/cas/login?service=http%3A%2F%2Fnew.kyivstar.ua%2Fecare%2F")
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys("0961451058")
        wd.find_element_by_css_selector("button.btn.btn-default").click()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").send_keys("MK2prod_2016")
        wd.find_element_by_xpath("//section[@id='section-left']/section[2]/div/div[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-default").click()
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
