from selenium import webdriver
from fixture.session import SessionHelper
from fixture.General.document_information import DocumentInformationHelp
from fixture.General.product_information import ProductInformationHelp
from fixture.General.supplier_information import SupplierInformationHelp
from fixture.General.applicable_and_attachments import ApplicableAndAttachmentInformationHelp


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.docinfo = DocumentInformationHelp(self)
        self.productinfo = ProductInformationHelp(self)
        self.supplierinfo = SupplierInformationHelp(self)
        self.appl_attach = ApplicableAndAttachmentInformationHelp(self)



    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("maintable")) > 0):
            wd.get(self.base_url)

    def edit_document(self):
        self.wd.find_element_by_xpath("//div[@class = 'ms-rtestate-field']/a").click()
        self.wd.find_element_by_xpath("//ul[@id='menu']//a[@class='editDocument']").click()

    def error_checker(self,section, label):
        wd = self.wd
        labels = wd.find_elements_by_xpath("//div[@id='leftMenuBar']//li[@class='node']/a")
        for element in labels:
            if label == element.text:
                current_element_index = int(labels.index(element)) + 1
                break
        counter = wd.find_element_by_xpath("//div[@id='leftMenuBar']//ul[%s]//li[%s]/span[@class='errorsCount']" % (section,current_element_index))
        if counter.text == '0':
            return True
        return False

    def identify_in_current_section(self):
        wd = self.wd
        current_section = wd.find_element_by_xpath("//div[@id='navigationBar']//a[@class='currentItem']").text
        return current_section





    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False