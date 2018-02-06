def test_login(app):
    app.open_home_page()
    app.edit_document()
    app.docinfo.add_revision('5A','New')
    app.docinfo.add_part_number('M210862A003', 'A')
