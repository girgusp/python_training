# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="test_first_name", middle_name="test_middle_name",
                            last_name="test_last_name", nickname="test_nickname", title="test_title",
                            company="test_company", address="test_address", home="test_home", mobile="test_mobile",
                            work="test_work", fax="test_fax", mail1="test_mail1", mail2="test_mail2",
                            mail3="test_mail3", homepage="test_homepage", address2="test_address", home2="test_home",
                            notes="test_notes"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="",
                            address="", home="", mobile="", work="", fax="", mail1="", mail2="", mail3="", homepage="",
                            address2="", home2="", notes=""))
    app.session.logout()
