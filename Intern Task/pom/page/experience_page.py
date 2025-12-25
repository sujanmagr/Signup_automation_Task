from selenium.webdriver.common.by import By
import time
class experience:
    def __init__(self, driver):
        self.driver=driver
    
    def fill_form(self, annually, area, focus):
        self.driver.find_element(By.XPATH,"//div[@dir='ltr']//div[3]").click()
        self.driver.find_element(By.NAME,"number_of_students_recruited_annually").send_keys(annual)
        self.driver.find_element(By.NAME,"focus_area").send_keys(area)
        self.driver.find_element(By.NAME,"success_metrics").send_keys(focus)
        self.driver.find_element(By.XPATH,"//button[@id='«rlh»-form-item']").click()

    def click_next(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()