from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def hello_mk(self):
        wd = self.wd
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://new.kyivstar.ua/ecare/")

    def destroy(self):
        self.wd.quit()