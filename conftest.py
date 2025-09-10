import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit browser"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
