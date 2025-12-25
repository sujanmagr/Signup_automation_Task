from selenium.webdriver.common.by import By
import time
class verification:
    def __init__(self, driver):
        self.driver=driver
    
    def fill_form(self, regno, certficate, file):
        self.driver.find_element(By.NAME,"business_registration_number").send_keys(regno)
        self.driver.find_element(By.NAME,"certification_details").send_keys(certificate)
        self.driver.find_element(By.XPATH,"//div[@class='h-full w-full rounded-//div//div[1]").click()

        self.driver.find_element(By.XPATH,"//div[@id='«rbl»-form-item']").send_keys(file)
        self.driver.find_elements(By.XPATH,"//button[normalize-space()='Submit']").click()
    def click_next(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()