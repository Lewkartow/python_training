__author__ = 'Алексей'

from model.group import Group

class GroupHelper:


    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        if (driver.current_url.endswith("/group.php")) and (len(driver.find_elements_by_name("New"))) > 0:
            return
        driver.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self, index):
        self.delete_group_by_index(0)
        self.group_cache = None

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, index):
        self.delete_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        driver.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


