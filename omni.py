from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(3)