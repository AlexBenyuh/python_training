from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.session import SessionHelper
from fixture.mk import MkHelper
from fixture.cas import CasHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.mk = MkHelper(self)
        self.cas = CasHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://new.kyivstar.ua/ecare/")
        wd.maximize_window()

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

