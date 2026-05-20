from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.contact_page import ContactPage

def test_valid_form_submission():
    print("\n--- Test 1: Valid Form Submission ---")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    page = ContactPage(driver)
    page.open()
    
    page.fill_name("John Silva")
    page.fill_email("john@gmail.com")
    page.fill_phone("+94771234567")
    page.fill_message("This is a test message for QA automation.")
    
    page.take_screenshot(os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'valid_form_filled.png'))
    
    page.click_submit()
    
    page.take_screenshot(os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'valid_form_submitted.png'))
    
    print("Test 1 Completed!")
    driver.quit()


def test_empty_form_submission():
    print("\n--- Test 2: Empty Form Submission ---")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    page = ContactPage(driver)
    page.open()
    
    page.click_submit_js()
    
    page.take_screenshot(os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'empty_form_error.png'))
    
    print("Test 2 Completed!")
    driver.quit()


if __name__ == "__main__":
    test_valid_form_submission()
    test_empty_form_submission()