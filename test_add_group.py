# -*- coding: utf-8 -*-
import wd as wd
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def create_group(group,):
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # submit group creation
    wd.find_element_by_name("submit").click()


def open_home_page(wd):
    wd.get("http://localhost/addressbook/addressbook/")


def open_groups_page(wd):
    wd.find_element_by_link_text("groups").click()


def login(wd, username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_groups_page(wd)
        create_group(wd, Group(name="name1", header="header1", footer="footer1"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_groups_page(wd)
        create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self, wd):
        self.wd.quit()

    def return_to_groups_page(wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()


if __name__ == '__main__':
    unittest.main()
