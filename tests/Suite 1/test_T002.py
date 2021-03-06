def test_t002(app):
    app.open_home_page()
    # check that documents are filtered to logged user authorship
    # where logged user is unique author in documents tables
    assert app.dashboard.get_current_logged_user() == app.dashboard.get_all_unique_authors()
    # input value to 'search' field
    app.dashboard.search('55')
    app.dashboard.search('My Documents')
    assert app.dashboard.get_current_logged_user() == app.dashboard.get_all_unique_authors()
