
class AdministrationMain:
    def __init__(self, app):
        self.app = app

    def navigate_to(self, section_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href and text()='%s']" % section_name).click()

    def get_all_unique_columns(self):
        wd = self.app.wd
        columns = sorted(set([i.text for i in wd.find_elements_by_xpath("//div[@id='ConfigurableValuesList']//th")]))
        for item in columns:
            if item == ' ':
                columns.remove(item)
        return columns

    def save_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//p[1]//span[@class='ui-button-text' and text()='Save']").click()
        self.app.wait()



