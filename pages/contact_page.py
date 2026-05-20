from selenium.webdriver.common.by import By
import time

class ContactPage:
    
    # URL
    URL = "https://safora.se/en/contact.html"
    
    # Locators
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PHONE_FIELD = (By.NAME, "phone")
    MESSAGE_FIELD = (By.NAME, "message")
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='rs-contact-btn']//button")
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)
        time.sleep(3)
    
    def fill_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)
        time.sleep(1)
    
    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        time.sleep(1)
    
    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        time.sleep(1)
    
    def fill_message(self, message):
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(message)
        time.sleep(1)
    
    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(3)

    def click_submit_js(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved — {filename}")