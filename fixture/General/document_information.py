class DocumentInformationHelp:
    def __init__(self,app):
        self.app = app


    def add_revision(self, revision_value, revision_descr):
        wd = self.app.wd
        if  self.app.identify_in_current_section()== 'Document Information':
            if self.app.error_checker('1', 'Document Information') == False:
                if len (wd.find_elements_by_xpath("//ul[@id='menu']//a[@class='editDocument' and @disabled = 'disabled']")) >= 1:
                    wd.find_element_by_xpath("//div[@id= 'readonlyRevisionTableContainer']//a[@href]").click()
                    wd.find_element_by_xpath("//div[@id = 'revisionTableContainer']//a[@href]").click()
                    wd.find_element_by_xpath("//tbody[@data-bind = 'foreach: RevisionTable.Revisions']//td[1]/input").click()
                    wd.find_element_by_xpath("//tbody[@data-bind = 'foreach: RevisionTable.Revisions']//td[1]/input").send_keys(revision_value)
                    wd.find_element_by_xpath("//tbody[@data-bind = 'foreach: RevisionTable.Revisions']//td[2]/input").click()
                    wd.find_element_by_xpath("//tbody[@data-bind = 'foreach: RevisionTable.Revisions']//td[2]/input").send_keys(revision_descr)
                    wd.find_element_by_xpath("//div[@id = 'revisionTableContainer']//span[@class='ui-button-text' and text()='OK']").click()
                    if len(wd.find_elements_by_xpath("//span[@class='ui-button-text' and text()='Spell check']")) >= 1:
                        wd.find_element_by_xpath("//span[@class='ui-button-text' and text()='Continue']").click()
                    wd.find_element_by_xpath("//ul[@id='menu']//a[text()='Save']").click()
                    wd.find_element_by_xpath('//div[@class="navigationPanel"]/a[text()="Next"]').click()
            else:
                wd.find_element_by_xpath('//div[@class="navigationPanel"]/a[text()="Next"]').click()
        else:
            pass



    def add_part_number(self,part_number,part_version):
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
                wd.find_element_by_xpath("//ul[@id='menu']//a[text()='Save']").click()
                wd.find_element_by_xpath('//div[@class="navigationPanel"]/a[text()="Next"]').click()
            else:
                wd.find_element_by_xpath('//div[@class="navigationPanel"]/a[text()="Next"]').click()
        else:
            pass









