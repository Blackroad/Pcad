from selenium import webdriver
from fixture.Docwriter.General.document_information import DocumentInformationHelp
from fixture.Docwriter.General.product_information import ProductInformationHelp
from fixture.Docwriter.General.supplier_information import SupplierInformationHelp
from fixture.Docwriter.General.applicable_and_attachments import ApplicableAndAttachmentInformationHelp
from fixture.Dashboard.dashboard import DashboardHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.config = config
        self.base_url = config['web']['baseURL']
        self.docinfo = DocumentInformationHelp(self)
        self.productinfo = ProductInformationHelp(self)
        self.supplierinfo = SupplierInformationHelp(self)
        self.dashboard = DashboardHelper(self)
        self.appl_attach = ApplicableAndAttachmentInformationHelp(self)

    def wait(self, element, wait_type='visible'):
        wd = self.wd
        wait = WebDriverWait(wd, 20)
        if wait_type == 'visible':
            wait.until(ec.visibility_of_element_located((By.XPATH, "%s" % element)))
        elif wait_type == 'click':
            wait.until(ec.element_to_be_clickable((By.XPATH, "%s" % element)))

    def change_active_tab(self):
        wd = self.wd
        active_tabs = wd.window_handles
        wd.switch_to.window(active_tabs[1])

    def get_active_tab(self):
        wd = self.wd
        current = wd.current_window_handle
        return current

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("PCAD/Dashboard") and
                len(wd.find_elements_by_xpath("//table[@class='allDocumentsTable']")) > 0):
            wd.get(self.base_url)

    def error_checker(self, section, label):
        wd = self.wd
        current_element_index = None
        labels = wd.find_elements_by_xpath("//div[@id='leftMenuBar']//li[@class='node']/a")
        for element in labels:
            if label == element.text:
                current_element_index = int(labels.index(element)) + 1
                break
        counter = wd.find_element_by_xpath("//div[@id='leftMenuBar']//ul[%s]//li[%s]/span[@class='errorsCount']" %
                                           (section, current_element_index))
        if counter.text == '0':
            return True
        return False

    def save_changes(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@id='menu']//a[text()='Save']").click()

    def next(self):
        wd = self.wd
        wd.find_element_by_xpath('//div[@class="navigationPanel"]/a[text()="Next"]').click()

    def identify_in_current_section(self):
        wd = self.wd
        current_section = wd.find_element_by_xpath("//div[@id='navigationBar']//a[@class='currentItem']").text
        return current_section

    def navigate_to(self, name_of_section):
        wd = self.wd
        try:
            wd.find_element_by_xpath("//*[@id='navigationBar']//a[@href and text()='%s']" % name_of_section)
        except Exception as e:
            print("Error as %s" % e)

    def skip_to(self, name_of_section):
        wd = self.wd
        last_clickable_element = self.get_last_clickable_section()
        # if element is clickable no need to skip
        if not len(wd.find_elements_by_xpath("//*[@id='navigationBar']//a[@href and text()='%s' "
                                             "and @style='display: none;']" % name_of_section)):
            wd.find_element_by_xpath("//*[@id='navigationBar']//a[@href and text()= '%s']" % name_of_section).click()
        elif not len(wd.find_elements_by_xpath("//*[@href and @class='currentItem' "
                                               "and text()='%s']" % last_clickable_element)):
            wd.find_element_by_xpath("//*[@id='navigationBar']//a[@href and text()= '%s']"
                                     % last_clickable_element).click()
            while not len(wd.find_elements_by_xpath("//*[@href and @class='currentItem' and text()='%s']"
                                                    % name_of_section)):  # while our section is not current-click Next
                self.next()

    def element_in_navigation_tree(self, element_name):
        wd = self.wd
        lst = wd.find_elements_by_xpath("//div[@id='navigationBar']//ul//a | /label[@style]")
        for i in lst:
            if i.text == element_name:
                return True
        return False

    def get_last_clickable_section(self):
        wd = self.wd
        lst = []
        sections_as_links = wd.find_elements_by_xpath("//div[@id='navigationBar']//ul//a "
                                                      "| /label[@style='display: none;']")
        for element in sections_as_links:
            if element.text == '':
                sections_as_links.pop(sections_as_links.index(element))
            else:
                lst.append(element.text)
        return lst[-1]

    def plan_b(self, name_of_element):
        wd = self.wd
        elem_index = None
        lst = wd.find_elements_by_xpath("//div[@id='navigationBar']//ul//a | /label[@style]")
        for elem in lst:
            if elem.text == name_of_element:
                elem_index = lst.index(elem)
        ul_index = self.get_ul_index(elem_index)
        for i in range((elem_index-1), 0):
            if len(wd.find_elements_by_xpath("//div[@id='navigationBar']//ul[%s]//li[%s]//a "
                                             "| /label[@style='display: none']" % (ul_index, elem_index))) > 0:
                wd.find_element("//div[@id='navigationBar']//ul[%s]//li[%s]//a "
                                "| /label[@style='display: none']" % (ul_index, elem_index)).click()
            pass

    @staticmethod
    def get_ul_index(elem_index):
        if elem_index in range(5):
            ul = 1
        elif elem_index in range(5, 10):
            ul = 2
        elif elem_index in range(11, 19):
            ul = 3
        elif elem_index in range(20, 21):
            ul = 4
        else:
            ul = 5
        return ul

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except Exception as e:
            print(e)
            return False
