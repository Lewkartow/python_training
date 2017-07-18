# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"

    def test_add_group(self):
        driver = self.driver
        driver.get(self.base_url + "addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("ABC")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("BCA")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("ZXC")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
