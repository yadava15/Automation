from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    # 1. Open the browser and navigate to the URL
    driver.get("http://practice.automationtesting.in/")

    # 2. Click on the My Account menu
    my_account_link = driver.find_element(By.LINK_TEXT, "My Account")
    my_account_link.click()

    # 3. Enter the registered username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("anil@gmail.com")

    # 4. Enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("pass1234")

    # 5. Click on the login button
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    time.sleep(3)  # Wait for the page to load

    print("Login successful!")

finally:
    # 7. Close the browser
    driver.quit()
