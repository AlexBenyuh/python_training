from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, credentials):
        wd = self.app.wd
        wd.wait = WebDriverWait(wd, 10)
        # self.app.open_home_page()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.login)
        self.wait_click(wd, css="button.btn.btn-default")
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.password)
        wd.find_element_by_xpath("//section[@id='section-left']/section[2]/div/div[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-default").click()

    def wait_click(self, wd, css):
        wd.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
        wd.find_element_by_css_selector(css).click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/div[4]/div[2]/div[3]/div/div[2]/div/a[2]").click()
