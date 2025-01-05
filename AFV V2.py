from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDrivers
driver = webdriver.Firefox()
driver.get("https://afvnew.vercel.app/")    # URL
driver.maximize_window()                    # Maximized Browser
time.sleep(2)                               # Wait for the page to load 

# Accepting Cookies
accept_button = driver.find_element(By.XPATH, '//button[normalize-space(text())="Accept All"]')
accept_button.click()
time.sleep(2)

# Locating the Login Button
button = driver.find_element(By.XPATH, "//button[@title='login']")
button.click()
  
# Inputting the Email address 
input_email = driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys("rodela@neoscoder.com") # "nam@nam.com" / "rodela@neoscoder.com"
time.sleep(1)
# Inputting the Password 
input_password = driver.find_element(By.XPATH,"//input[@aria-label='Password']").send_keys("Afv@123456789")
time.sleep(1)

# Clicking LogIn Button 
login_button = driver.find_element(By.XPATH,"//button[@type='button' and text()='Log In']")
if login_button.is_enabled():
    login_button.click()
time.sleep(5)

'''

# Selecting Product Button
product_button = driver.find_element(By.XPATH,"//a[text()='Products']")
product_button.click()
time.sleep(2)

# Selecting Checkbox
driver.find_element(By.XPATH,"//label[normalize-space()='Beverage']").click()
time.sleep(2)

# Inputting Maximum Rate Amount
input_element = driver.find_element(By.XPATH, "//input[@aria-label='Max']")
for _ in range(5):
    input_element.send_keys(Keys.BACK_SPACE)

input_element.send_keys("2000")
time.sleep(2)

# Searching Product
input_element = driver.find_element(By.XPATH,"//input[@aria-label='Search products...']").send_keys("Mojo")
time.sleep(2)

# Adding product into Cart
button = driver.find_element(By.XPATH,"//button[@type='button' and text()='Add to Cart']")
button.click()
time.sleep(2)

# Clearing Product Name
input_element = driver.find_element(By.XPATH,"//input[@aria-label='Search products...']")
for _ in range(4):
    input_element.send_keys(Keys.BACK_SPACE)
time.sleep(2)

# Searching Product
input_element = driver.find_element(By.XPATH,"//input[@aria-label='Search products...']").send_keys("Mango")
time.sleep(2)

# Adding product into Cart
button = driver.find_element(By.XPATH,"//button[@type='button' and text()='Add to Cart']")
button.click()
time.sleep(2) 
'''
'''
# Clicking Cart Option
button = driver.find_element(By.XPATH, '//button[contains(@class, "bg-green-600") and contains(@class, "rounded-full")]')
button.click()
time.sleep(2)

# Picked Class for ScrollBar
cart_element = driver.find_element(By.XPATH,"//div[contains(@class, 'custom-scrollbar')]")

# Scroll down by 10000 pixels
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 10000", cart_element)

#increase_button = driver.find_element(By.XPATH, "(//button[.//svg//path[contains(@d, 'M416')]])[2]")
#increase_button.click()

# Proceed to Checkout Button Click
checkout_button = driver.find_element(By.XPATH,"//button[@type='button' and text()='Proceed to Checkout']")
checkout_button.click()
time.sleep(2)
'''
'''
#----------This portion for New user
# Selecting Address Type
address_type=driver.find_element(By.XPATH, "//button[.//label[text()='Address Type']]")
address_type.click()
time.sleep(1)

# Selecting Office Option
office_option = driver.find_element(By.XPATH, "//li[.//span[text()='Office']]")
office_option.click()

# Selecting District Button
address_type=driver.find_element(By.XPATH, "//button[.//label[text()='District']]")
address_type.click()
time.sleep(1)

# Selecting Address Option
office_option = driver.find_element(By.XPATH, "//li[.//span[text()='Dhaka']]")
office_option.click()

# Selecting Thana Button
address_type=driver.find_element(By.XPATH, "//button[.//label[text()='Thana']]")
address_type.click()
time.sleep(1)

# Selecting Thana Option
office_option = driver.find_element(By.XPATH, "//li[.//span[text()='Dhanmondi']]")
office_option.click()

# Input Postal Code
postal_code = driver.find_element(By.XPATH,"//input[@aria-label='PostalCode']").send_keys("1209")
time.sleep(2) 

# Input Address
address_input = driver.find_element(By.XPATH,"//input[@aria-label='Address']").send_keys("Beside Bosundhara City,19/1/ka,Akij Food and Beverage Limited")
'''
'''
# Delivery information Select
delivery_buttoon = driver.find_element(By.XPATH,"//p[text()='Office Address']")
delivery_buttoon.click()
time.sleep(2)

# Online Payment Selection
online_payment_label = 'Online Payment'  # 'Cash on Delivery' / 'Online Payment'
online_payment_button=driver.find_element(By.XPATH,f"//label[normalize-space()='{online_payment_label}']")
online_payment_button.click()
time.sleep(2)

if online_payment_label == 'Online Payment':  # Check if Online Payment is selected
    # If selected then Continue button
    continue_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Continue']")
    continue_button.click()
else:
    # If not selected then Place Order button
    #place_order_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Place Order']")
    #place_order_button.click()

    place_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and text()='Place Order']"))
    )
    place_order_button.click() 

### Online Payment Information ###

card_no = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Card Number']"))
)
card_no.send_keys("371111111111111")
time.sleep(2)

exp_year = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "expiry"))
)
exp_year.send_keys("12/26")
time.sleep(2)

cvc = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID,"email"))
)
cvc.send_keys("123")
time.sleep(2)

card_holder = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Card Holder Name']"))
)
card_holder.send_keys("Rodela")
time.sleep(2)

pay_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'loading-btn') and .//span[contains(text(), 'Pay')]]"))
)
pay_button.click()
time.sleep(2)

success_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Success']"))
)
success_button.click()
time.sleep(5)
'''

'''
# Checking Order View
viewOrder_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='View Order']"))
)
viewOrder_button.click()

'''
'''
# Going Back to Home
gohome_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//button[@type='button' and text()='Go Home']"))
)
gohome_button.click()
'''

# Clicking on Profile
profile_button = driver.find_element(By.XPATH,"//button[starts-with(@id, 'react-aria')]")
profile_button.click()
time.sleep(2)

# Log Out Button
logout_button = driver.find_element(By.XPATH, "//li[.//span[text()='Log Out']]")
logout_button.click()








#card_no = driver.find_element(By.ID, "ccnum").send_keys("371111111111111")
#exp_year = driver.find_element (By.ID,"expiry").send_keys("1226")
#cvc = driver.find_element (By.ID,"email").send_keys("123")
#card_holder = driver.find_element(By.XPATH,"//input[@placeholder='Card Holder Name']").send_keys("Rodela")
#pay_button=driver.find_element(By.XPATH, "//button[.//span[text()='Pay']]")
#pay_button.click()

