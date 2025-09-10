from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

import time

class PIMPage(BasePage):
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_EMPLOYEE = (By.XPATH, "//a[text()='Add Employee']")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    EMPLOYEE_LIST = (By.LINK_TEXT, "Employee List")

    def go_to_pim(self):
        pim = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PIM_MENU))
        pim.click()

    def add_employee(self, fname, lname):
        self.click(self.ADD_EMPLOYEE)
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.click(self.SAVE_BTN)
        time.sleep(2)

    def verify_employee_in_list(self, name):
        self.click(self.EMPLOYEE_LIST)
        time.sleep(2)
        return name in self.driver.page_source

    def go_to_employee_list(self):
        self.driver.find_element(By.LINK_TEXT, "Employee List").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']")))
