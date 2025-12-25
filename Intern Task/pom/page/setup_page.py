# for setup page
from selenium.webdriver.common.by import By
import time
class SetupPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, fname, lname, email,  phone,  password):
        self.driver.find_element(By.NAME, "firstName").send_keys(fname)
        time.sleep(1)
        self.driver.find_element(By.NAME, "lastName").send_keys(lname)
        time.sleep(1)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.NAME,"phoneNumber").send_keys(phone)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='confirmPassword']").send_keys(password)
        time.sleep(1)
    
    def click_next(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()

