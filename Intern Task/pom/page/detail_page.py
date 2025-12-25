from selenium.webdriver.common.by import By
import time
class detail:
    def __init__(self, driver):
        self.driver=driver
        self.driver.find_element
    
    def fill_form(self,name, role, email, website, address):
        self.driver.find_element(By.NAME,"agency_name").send_keys(name)
        self.driver.find_element(By.NAME,"role_in_agency").send_keys(role)
        self.driver.find_element(By.NAME,"agency_email").send_keys(email)
        self.driver.find_element(By.NAME,"agency_website").send_keys(website)
        self.driver.find_element(By.NAME,"agency_address").send_keys(address)
        self.driver.find_element(By.XPATH,"//span[@class='font-satoshi-regular text-translucent']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[@class='h-full w-full rounded-//div//div[1]").click()

    def click_next(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()



