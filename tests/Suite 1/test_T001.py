def test_t001(app):
    app.open_home_page()
    # verify elements presenting
    assert app.dashboard.element_presented(dashboard="//table[@class='allDocumentsTable']",
                                           published_dashboard="//fieldset[@class='publishedDocumentsCont']",
                                           home_btn="//ul[@id='menu']//a[@href and text()='Home']",
                                           admin_btn="//ul[@id='menu']//a[@href and text()='Administration']",
                                           my_documents_btn="//input[@type='button' and @value = 'My Documents']",
                                           add_new_btn="//div[@class='addNewDocBtnCont']/a",
                                           search_btn="//input[@type='button' and @value = 'Search']",
                                           edit_btn="//tr[1]//a[text()='Edit']") is True  # dashboard is displayed
    # get headers from doc_table
    headers_from_doc_table = [i.text for i in (app.wd.find_elements_by_xpath("//table[@class='allDocumentsTable']"
                                                                             "//th[text()]"))]
    assert headers_from_doc_table == ['Document Id', 'Title', 'Author', 'Date Created▲']
    headers_from_publish_table = [i.text for i in (app.wd.find_elements_by_xpath("//fieldset[@class='publishedDocumentsCont']//th[text()]"))]
    assert headers_from_publish_table == ['Name', 'Version', 'RL', 'Modified', 'Modified By']
    assert app.dashboard.check_sorting('Date Created', 'Document Id', 'Title', 'Author') is True
    app.dashboard.search()  # to return a set of all documents
    app.dashboard.paging('>', '>>', '<', '<<')  # navigates through pages
    app.dashboard.open_administration()
    app.dashboard.open_home()
    app.dashboard.edit_document()  # clicks on random document to open docwriter editor
    assert app.dashboard.element_presented(docwriter="//div[@id = 'navigationBar']") is True  # verify that docwriter is opened













