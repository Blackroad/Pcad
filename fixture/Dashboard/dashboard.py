import random


class DashboardHelper:
    def __init__(self, app):
        self.app = app

    def edit_document(self, doc_number=None):
        wd = self.app.wd
        set_of_docs = wd.find_elements_by_xpath("//table[@class='allDocumentsTable']//td[@class='break-initial']/a[@href and text()='Edit']")
        if doc_number is None:
            random.choice(set_of_docs).click()
            self.app.change_active_tab()
            self.app.wait("//a[@class = 'section' and text()='General Section']")

    def search(self, search_value=None):
        wd = self.app.wd
        if search_value is None:
            wd.find_element_by_xpath("//input[@placeholder='Search documents']").clear()
        elif search_value == 'My Documents':
            wd.find_element_by_xpath("//input[@value = 'My Documents']").click()
        else:
            wd.find_element_by_xpath("//input[@placeholder='Search documents']").clear()
            wd.find_element_by_xpath("//input[@placeholder='Search documents']").send_keys(search_value)
        wd.find_element_by_xpath("//input[@value='Search']").click()
        self.app.wait("//a[@href and text()='Edit']")

    def apply_sorting(self, column_name):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//th[text()='%s']" % column_name)) == 0:
            if len(wd.find_elements_by_xpath("//th[text()='%s▲']" % column_name)) == 0:
                wd.find_element_by_xpath("//th[text()='%s▼']" % column_name).click()
            else:
                wd.find_element_by_xpath("//th[text()='%s▲']" % column_name).click()
        else:
            wd.find_element_by_xpath("//th[text()='%s']" % column_name).click()

    def check_sorting(self, *columns_name):
        for item in columns_name:
            if item == 'Document Id':
                self.apply_sorting("Document Id")
                if not self.column_is_sorted("//td[@data-bind='text: RecordId']"):
                    return False
            elif item == 'Title':
                self.apply_sorting("Title")
                if not self.column_is_sorted("//td[@data-bind='text: Title']"):
                    return False
            elif item == 'Author':
                self.apply_sorting("Author")
                if not self.column_is_sorted("//td[@data-bind='text: Author']"):
                    return False
            elif item == 'Date Created':
                self.apply_sorting("Date Created")
                if not self.column_is_sorted("//td[@data-bind='text: CreatedOn']"):
                    return False
        return True

    def column_is_sorted(self, column_xpath):
        wd = self.app.wd
        generated_list = [elem.text for elem in (wd.find_elements_by_xpath(column_xpath))]
        sorted_list = []
        for elem in wd.find_elements_by_xpath(column_xpath):
            sorted_list.append(elem.text)
        if sorted_list == sorted(generated_list, key=lambda s: s.lower()) \
                or sorted(generated_list, key=lambda s: s.lower(), reverse=True) \
                or generated_list:
            return True
        else:
            return False

    def paging(self, *page_controls):
        wd = self.app.wd
        for control in page_controls:
            wd.find_element_by_xpath("//div[@class='paging-container']/span[text()='%s']" % control).click()
        self.app.wait("//a[@href and text()='Edit']")

    def open_home(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href and text()='Home']").click()
        self.app.wait("//table[@class='allDocumentsTable']")

    def open_administration(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//a[@href and text()='Administration']")) == 0:
            print('No element(s) was found')
        else:
            wd.find_element_by_xpath("//a[@href and text()='Administration']").click()

    def add_new_document(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//a[@href and text()='Add New']")) == 0:
            print('No element(s) was found')
        else:
            wd.find_element_by_xpath("//a[@href and text()='Add New']").click()

    def get_current_logged_user(self):
        wd = self.app.wd
        user = wd.find_element_by_xpath("//div[@class='userName']")
        return user.text

    def get_all_unique_authors(self):
        wd = self.app.wd
        authors = set([i.text for i in wd.find_elements_by_xpath("//div//fieldset[@class='float-left allDocumentsCont']//td[3]")])
        for item in authors:
            authors = (' '.join(item.split(' ')[0:2]))
        return authors
