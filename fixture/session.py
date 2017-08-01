
class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, credentials):
        wd = self.app.wd
        # self.app.open_home_page()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.login)
        wd.find_element_by_css_selector("button.btn.btn-default").click()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").send_keys(credentials.password)
        wd.find_element_by_xpath("//section[@id='section-left']/section[2]/div/div[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-default").click()

    def logout(self) -> object:
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/div[4]/div[2]/div[3]/div/div[2]/div/a[2]").click()