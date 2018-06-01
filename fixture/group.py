class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
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
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group to delete
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group to edit
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # edit fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(" added to name")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(" added to header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(" added to footer")

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()