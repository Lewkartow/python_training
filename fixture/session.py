__author__ = 'Алексей'
from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()


"""    def if_not_logout(self):
        driver = self.app.driver
        if driver.find_element("logout") != 0:
             try:
                 driver.find_element_by_link_text("Logout").click()
             except:
                 pass
        else:
            pass
"""

