from model.credentials import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MkHelper:

    def __init__(self, app):
        self.app = app

    def hello_mk(self):
        wd = self.app.wd
        wd.wait = WebDriverWait(wd, 10)
        wd.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.header-bar__logo-img")))
        #wd.find_element_by_css_selector("a.header-bar__logo-img").click()

    def merge_from_mk(self):
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/div[4]/div[2]/div[4]/div/div[2]/span").click()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").click()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").clear()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").send_keys(multiplelogin)
        wd.find_element_by_xpath(".//*[@id='addSubscription']/div/div/div[2]/form/div[2]/div/div/div/div/div[2]/button").click()
        wd.wait = WebDriverWait(wd, 10)
        wd.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".info-block__wrapper.not-found__wrapper")))
        print(wd.current_url)
