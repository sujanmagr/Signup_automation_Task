from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.common.keys import Keys
from pom.page.detail_page import detail
from pom.page.setup_page import SetupPage
from pom.page.experience_page import experience
from pom.page.verification_page import verification
from data.data_generator import get_otp_from_guerrillamail, random_fname, random_lname, random_number, random_password, random_role, random_website, random_address, random_email

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://authorized-partner.vercel.app/register?step=setup")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_setup(driver):
    fname = random_fname()
    lname = random_lname()
    email = "ywyvjjwm@sharklasers.com"
    phone = random_number()
    password = random_password()


    # Setup detail page
    setup_page = SetupPage(driver)
    setup_page.fill_form(fname, lname, email, phone, password)
    time.sleep(2)
    setup_page.click_next()
    time.sleep(2)
    time.sleep(10)  # Wait for the OTP to arrive in the mailbox

    # Fetch OTP from Guerrilla Mail inbox
    otp = get_otp_from_guerrillamail("ywyvjjwm")  # Provide the email part before '@'

    if otp is None:
        print("Failed to get OTP.")
        return

    print(f"OTP received: {otp}")

    # Switch back to the main form tab (if required)
    driver.switch_to.window(driver.window_handles[0])

    # Fill the OTP field in the form
    otp_field = driver.find_element(By.XPATH, "//input[@id='otpField']")
    otp_field.send_keys(otp)

    # Click the submit button
    submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/div/div[2]/div/form/div[2]/button")  # Replace with the correct XPath for the submit button
    submit_button.click()  # Click on the submit button

    time.sleep(4)  # Wait for the next step to load after submission

    fname=random_fname()
    lname=random_lname()
    full_name = f"{fname} {lname}"
    role=random_role()
    email=random_email()
    website=random_website()
    address=random_address()
#detail page
    detail_page=detail(driver)
    detail_page.fill_form(full_name, role, email, website, address)
    detail_page.click_next()
    time.sleep(1)
#experience page
    experience_page=experience(driver)
    experience_page.fill_form(3,"nagarjun", 4)
    experience_page.click_next()
    time.sleep(1)
    #verification
    verification_page=verification(driver)
    regno=98372123
    certificate="usa based"
    file=r"C:\Users\Bhabisara Budhathoki\Desktop\sdmn.pdf"
    verification_page.fill_form(regno, certificate, file)
    time.sleep(1)
    verfication_page.click_next()





