# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def test_untitled_test_case(self):
        dw = self.dw
        self.open_home_page(dw)

        self.login(dw)

        self.open_groups_page(dw)

        self.create_group(dw)

        self.return_groups_page(dw)

        self.logout(dw)

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def return_groups_page(self, dw):
        dw.find_element_by_link_text("groups").click()

    def create_group(self, dw):
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys("kek3")
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys("kek3")
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys("kek3")
        dw.find_element_by_name("submit").click()

    def open_groups_page(self, dw):
        dw.find_element_by_name("new").click()

    def login(self, dw):
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").click()
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, dw):
        dw.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try:
            self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.dw.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
