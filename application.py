from selenium.webdriver.chrome.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def hello_mk(self):
        wd = self.wd
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()

    def login(self, credentials):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.login)
        wd.find_element_by_css_selector("button.btn.btn-default").click()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.password)
        wd.find_element_by_xpath("//section[@id='section-left']/section[2]/div/div[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-default").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://new.kyivstar.ua/ecare/")

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("html/body/div[4]/div[2]/div[3]/div/div[2]/div/a[2]").click()

    def destroy(self):
        self.wd.quit()