# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        driver = self.driver
        self.open_home_page(driver)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # fill group form
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def logout(self):
        # logout
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="ABC", header="BCA", footer="ZXC"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
