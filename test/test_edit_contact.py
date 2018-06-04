from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_first_name", middle_name="test_middle_name",
                                   last_name="test_last_name", nickname="test_nickname", title="test_title",
                                   company="test_company", address="test_address", home="test_home",
                                   mobile="test_mobile", work="test_work", fax="test_fax", mail1="test_mail1",
                                   mail2="test_mail2", mail3="test_mail2", homepage="test_homepage",
                                   address2="test_address", home2="test_home2", notes="test_notes"))
    app.contact.edit_first_contact()