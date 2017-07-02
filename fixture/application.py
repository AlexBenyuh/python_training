from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.mk import MkHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.mk = MkHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("https://new.kyivstar.ua/ecare/")

    def destroy(self):
        self.wd.quit()