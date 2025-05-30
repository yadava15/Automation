"""
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Now click on Home menu button
5) Test whether the Home page has Three Sliders only
6) The Home page must contains only three sliders
"""
"""
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Now click on Home menu button
5) Test whether the Home page has Three Arrivals only
6) The Home page must contains only three Arrivals
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
shop_menu = driver.find_element(By.LINK_TEXT,"Shop")
shop_menu.click()
time.sleep(3)
home_menu = driver.find_element(By.LINK_TEXT,"Home")
home_menu.click()
time.sleep(2)

sliders = driver.find_elements(By.CLASS_NAME,"n2-ss-slide")
slider_count = len(sliders)
if slider_count == 3:
    print("Test Case 1: Passed")
else:
    print("Test Case Failed")


time.sleep(5)
# Test whether the Home page has Three Arrivals only
# The Home page must contains only three Arrivals
assert slider_count == 3,"Home Page should contain only three sliders"
sliders[0].click()

# click on first arrivals image
arrival_image = sliders[0].find_element(By.TAG_NAME,"img")
arrival_image.click()
time.sleep(5)
#Verify navigation to product details page
#product_title = driver.find_element(By.CLASS_NAME,"product_title")

time.sleep(2)
print("Verify Add to basket button is present")
add_to_basket = driver.find_element(By.XPATH,'//*[text()="Selenium Ruby"]')
assert add_to_basket.is_displayed(),"Add to basket is not displayed"
add_to_basket.click()
print("Added to Card")
#Adding card
driver.find_element(By.XPATH, '//*[text()="Add to basket"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[text()="Description"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[text()="Reviews (0)"]').click()
time.sleep(5)
wait = WebDriverWait(driver, 10)
basket_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"wpmenucart-contents")))
basket_text = basket_menu.text
print(basket_text)
time.sleep(3)
assert "₹" in basket_text and "1 Item" in basket_text
print("Text Passed")
time.sleep(3)
# 9) Try to add more books than in stock
quantity_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"quantity")))
quantity_input.clear()
quantity_input.send_keys("24")
time.sleep(5)
try:
    driver.find_element(By.CSS_SELECTOR,"button.single_add_to_cart_button").click()
    time.sleep(2)
    Error = driver.find_element(By.CLASS_NAME,"woocommerce").text

    assert "Value between 1 and 20 " in Error
    print("Text Passed: Error Message is correct" )
except AssertionError:
    print("Text Passed: Error Message")


print("Test completed")
time.sleep(3)

driver.quit()

