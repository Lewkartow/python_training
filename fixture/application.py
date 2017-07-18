from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self, driver):
        driver = self.driver
        driver.get("http://localhost/addressbook/")


    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        driver = self.driver
        self.open_groups_page()
        #init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(Group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(Group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(Group.footer)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()


    def destroy(self):
        self.driver.quit()