
class MkHelper:

    def __init__(self, app):
        self.app = app

    def hello_mk(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()