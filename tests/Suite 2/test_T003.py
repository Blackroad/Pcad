from fixture.db_core import DBcore


def test_t003(app):
    db = DBcore()
    app.open_home_page()
    app.dashboard.open_administration()
    # admin opens Configurable Values by default
    assert app.element_presented(save_btn="//span[text()='Save']", category_filter="//select[@class='filter-category']",
                                 add_new_btn="//a[@href and text()='Add new value']", delete_value_btn="//a[@class = 'DeleteItemButton']")
    assert app.administration.get_all_unique_columns() == sorted(['Key', 'Value'])
    # compare lists in categories
    assert app.configurable_values.get_all_categories() == sorted(['CCD Governing Documents',
                                                                   'CFI table Data Type List',
                                                                   'CFI table Risk Level Export List',
                                                                   'CFI table Risk Level List', 'CFI table Sample Size List',
                                                                   'CFI table Target Requirements List', 'CFI table Target Type List',
                                                                   'CFI table Tolerance Interval Spec Window List', 'Compliant Systems List',
                                                                   'Component Quality Risk Values', 'Default Reference Documents',
                                                                   'Default Resource Documents',
                                                                   'Destructive Variable Reproducibility Study StdDev ratio list',
                                                                   'Disposition of failure Types', 'Electronic Storage Systems',
                                                                   'ERA table Data Type List', 'ERA table Sample Size List',
                                                                   'ERA table Target Type List', 'Lot Rationale Types',
                                                                   'Manual Deviation Types', 'Measurement Requirements Acceptance Requirement list',
                                                                   'Measurement Requirements System Analysis list', 'Medtronic Facility',
                                                                   'Medtronic Falicity', 'MSU Pass Fail list', 'Other', 'Pass Fail list',
                                                                   'Plant Number',
                                                                   'Product Acceptance Storages', 'Qualification Performing List',
                                                                   'Reference Attachment prefix list', 'Reference Documents Patterns list',
                                                                   'Rel Demo Lot Rationale Types', 'Reliability Perform List', 'Yes No list'],
                                                                  key=lambda s: s.lower())
    # compare DB list categories with adminUI list categories - should be equal
    assert db.get_configurable_values_category() == app.configurable_values.get_all_categories()
    app.configurable_values.add_new_cv_value('Yes No list', '', '')
    app.configurable_values.change_values('Yes No list', '3', '1')
    app.configurable_values.delete_value('Yes No list')
