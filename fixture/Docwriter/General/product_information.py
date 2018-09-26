class ProductInformationHelp:
    def __init__(self,app):
        self.app = app

    def add_part_number(self,part_number,part_version,title):
        wd = self.app.wd
        if self.app.identify_in_current_section() == 'Product Information':
            if self.app.error_checker('1', 'Product Information') == False:
                wd.find_element_by_xpath("//div[@id = 'partNumberBindingContainer']//span[@class='ui-button-text' and text()='Add']").click()
                wd.find_element_by_xpath("//div[@id='partNumberDialog']//input[@data-bind='value: PartNumberControl.partNumbersToEdit']").click()
                wd.find_element_by_xpath(
                    "//div[@id='partNumberDialog']//input[@data-bind='value: PartNumberControl.partNumbersToEdit']").send_keys(part_number)
                wd.find_element_by_xpath("//div[@id = 'partNumberDialog']//span[@class='ui-button-text' and text()='OK']").click()
                wd.find_element_by_xpath(
                    "//tbody[@data-bind = 'foreach: PartNumbers']//td[5]/input").send_keys(part_version)
                wd.find_element_by_xpath("//tbody[@data-bind = 'foreach: PartNumbers']//td[6]/input").send_keys(title)
                self.app.save_changes()
                self.app.next()
            else:
                self.app.next()
        else:
            pass