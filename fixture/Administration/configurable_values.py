class ConfigurableValuesHelper:
    def __init__(self, app):
        self.app = app

    def get_all_categories(self):
        wd = self.app.wd
        categories = sorted([i.text for i in wd.find_elements_by_xpath("//select[@class='filter-category']//option[text()!='All']")],
                            key=lambda s: s.lower())
        return categories

    def add_new_cv_value(self, category_name, key, value):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//a[@href and text()='Add new value']"
                                 % self.get_category_index(category_name)).click()
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//table//tr[@class='viewItem'][last()]"
                                 % self.get_category_index(category_name)).click()
        self.change_values(category_name, key, value)




    def change_values(self, category_name, key, value):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='editItem' "
                                 "and @style='display: table-row;']//tr[1]//input" % self.get_category_index(category_name)).clear()
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='editItem' "
                                 "and @style='display: table-row;']//tr[1]//input" % self.get_category_index(category_name)).send_keys(key)
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='editItem' "
                                  "and @style='display: table-row;']//tr[2]//input" % self.get_category_index(category_name)).clear()
        wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='editItem' "
                                  "and @style='display: table-row;']//tr[2]//input" % self.get_category_index(category_name)).send_keys(value)
        self.app.administration.save_page()

    def get_category_index(self, category_name):
        wd = self.app.wd
        list_of_categories = wd.find_elements_by_xpath("//div[@id='ConfigurableValuesList']//h4")
        index = None
        for elem in list_of_categories:
            if elem.text == category_name:
                index = int(category_name.index(elem.text)) + 1
        return index

    def validation_errors(self):
        wd = self.app.wd
        self.app.wait("//fieldset[@id='FormValidationSummary']")
        if len(wd.find_elements_by_xpath("//fieldset[@id='FormValidationSummary']//ul[text()]")) == 0:
            return False
        else:
            return True

    def list_of_category_values(self, category_name):
        wd = self.app.wd
        index = self.get_category_index(category_name)
        list = wd.find_elements_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='viewItem']/td[text()]" % index)
        gen_list = [i.text for i in list]
        return gen_list

    def delete_value(self, category_name, value_index=None):
        wd = self.app.wd
        items_count = len(wd.find_elements_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='viewItem']/td/a[@class='DeleteItemButton']" % self.get_category_index(category_name)))
        if value_index is None:
            wd.find_element_by_xpath("//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='viewItem'][last()]/td/a[@class='DeleteItemButton']" %
                                     (self.get_category_index(category_name))).click()
        elif value_index is not None:
            if value_index in range(items_count):
                wd.find_element_by_xpath(
                    "//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='viewItem'][%d]/td/a[@class='DeleteItemButton']" %
                    (self.get_category_index(category_name), value_index)).click()
            else:
                wd.find_element_by_xpath(
                    "//div[@id='ConfigurableValuesList']/div[%s]//tr[@class='viewItem'][last()]/td/a[@class='DeleteItemButton']" %
                    self.get_category_index(category_name)).click()
        self.app.wait()
        self.app.allert_action('Yes')
        self.app.administration.save_page()


