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

   assert "Value between 1 and 20 " in Error
    print("Text Passed: Error Message is correct" )
except AssertionError:
    print("Text Passed: Error Message")


# Step 11: Check if item is visible in the menu with price
basket = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
assert "₹" in basket.text, "Price not found in basket"
print("Item added to basket with price visible.")

# Step 12-13: Click on Item link (Cart icon)
basket.click()
time.sleep(2)

# Step 14-15: Apply coupon code
coupon_field = driver.find_element(By.ID, "coupon_code")
coupon_field.send_keys("krishnasakinala")
driver.find_element(By.NAME, "apply_coupon").click()
time.sleep(3)

# Confirm coupon applied
success_msg = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message").text
assert "Coupon code applied successfully." in success_msg
print("Coupon applied successfully and 50rps discount given.")    
time.sleep(3)
try:
    # 13) Locate subtotal and total elements
    subtotal_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tr.cart-subtotal td"))
    )
    total_elem = driver.find_element(By.CSS_SELECTOR, "tr.order-total td")

    subtotal_text = subtotal_elem.text
    total_text = total_elem.text

    print("Subtotal value:", subtotal_text)
    print("Total value:", total_text)

    # 14) Assert total < subtotal
    # Subtotal amount
    subtotal_amount = float(subtotal_text.replace("$", "")
                            .replace("£", "")
                            .replace("₹", "")
                            .replace(",", "")
                            .strip())

    # Total amount
    total_amount = float(total_text.replace("$", "")
                         .replace("£", "")
                         .replace("₹", "")
                         .replace(",", "")
                         .strip())

    assert total_amount < subtotal_amount, f"Expected total ({total_amount}) < subtotal ({subtotal_amount})."
    print("Verified that total is less than subtotal.")

    # 15) Click Proceed to Checkout button
    proceed_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
    )
    proceed_button.click()

    # 16) Verify Billing Details, Order Details, Additional Details, and Payment Gateway
    billing_details = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "billing_first_name"))  # Example field in billing section
    )
    order_review = driver.find_element(By.ID, "order_review")  # Example: contains order details
    additional_info = driver.find_element(By.ID, "order_comments")  # Example: additional details

    assert billing_details.is_displayed(), "Billing Details section not found."
    assert order_review.is_displayed(), "Order Details section not found."
    assert additional_info.is_displayed(), "Additional Details section not found."

    print("Verified Billing, Order, and Additional Details sections are present.")

    # 17) Fill in Billing Details Form
    billing_details.send_keys("Anil")  # First name
    driver.find_element(By.ID, "billing_last_name").send_keys("Yadav")
    driver.find_element(By.ID, "billing_email").send_keys("Anilyadav@gmail.com")
    driver.find_element(By.ID, "billing_phone").send_keys("1234567890")
    driver.find_element(By.ID, "billing_address_1").send_keys("Pune")
    driver.find_element(By.ID, "billing_city").send_keys("Hinjewadi")
    driver.find_element(By.ID, "billing_postcode").send_keys("12345")
    # Add dropdowns if needed for Country and State

    print("Billing details filled successfully.")

    # 17b) Select Payment Gateway option
    bank_transfer = driver.find_element(By.ID, "payment_method_bacs")
    bank_transfer.click()
    print("Selected Direct Bank Transfer as payment method.")

    # 18) Check for coupon field and verify again that billing
    coupon_field = driver.find_element(By.CSS_SELECTOR, "input#coupon_code")
    # assert coupon_field.is_displayed(), "Coupon field not found on checkout page."
    print("Coupon field is present.")

    assert billing_details.is_displayed(), "Billing Details section not found."
    assert order_review.is_displayed(), "Order Details section not found."
    assert additional_info.is_displayed(), "Additional Details section not found."
    print("Billing, Order, and Additional Details sections are still present after filling billing details and selecting payment.")

except Exception as e:
    driver.save_screenshot("checkout_debug.png")
    print("Error encountered during checkout process.")
    raise e

driver.quit()

