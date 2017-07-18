# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
          driver.get("http://localhost/addressbook/")

    def login(self, driver):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def create_group(self, driver):
        # fill group form
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("ABC")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("BCA")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("ZXC")
        driver.find_element_by_name("submit").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()


    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_groups_page(driver)
        self.create_group(driver)
        self.return_to_groups_page(driver)
        self.logout(driver)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
