
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_add_and_verify_employees(driver):
    login_page = LoginPage(driver)
    pim_page = PIMPage(driver)

    login_page.login("Admin", "admin123")
    pim_page.go_to_pim()

    employees = [("dev", "Man"), ("jack", "Jas"), ("lucy", "Son")]
    for fname, lname in employees:
        pim_page.add_employee(fname, lname)

    for fname, lname in employees:
        full_name = fname + " " + lname
        assert pim_page.verify_employee_in_list(full_name)
        print(f"{full_name} → Name Verified")
