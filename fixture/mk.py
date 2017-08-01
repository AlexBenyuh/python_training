
class MkHelper:

    def __init__(self, app):
        self.app = app

    def hello_mk(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.header-bar__logo-img").click()

    def merge_from_mk(self):
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/div[4]/div[2]/div[4]/div/div[2]/span").click()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").click()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").clear()
        wd.find_element_by_css_selector(".kstar-form__input.kstar-form__input").send_keys("0961451058")
        wd.find_element_by_xpath(".//*[@id='addSubscription']/div/div/div[2]/form/div[2]/div/div/div/div/div[2]/button").click()