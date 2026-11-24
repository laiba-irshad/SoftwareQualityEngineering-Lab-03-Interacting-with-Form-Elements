from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open registration form
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# Enter First Name
driver.find_element(By.ID, "firstName").send_keys("Shakir")

# Enter Last Name
driver.find_element(By.ID, "lastName").send_keys("Hussain")

# Enter Email
driver.find_element(By.ID, "userEmail").send_keys("shakir@example.com")

# Select Gender
driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()

# Enter Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("3001234567")

time.sleep(2)

# Verify entered values
print("First Name:", driver.find_element(By.ID, "firstName").get_attribute("value"))
print("Last Name:", driver.find_element(By.ID, "lastName").get_attribute("value"))
print("Email:", driver.find_element(By.ID, "userEmail").get_attribute("value"))
print("Mobile:", driver.find_element(By.ID, "userNumber").get_attribute("value"))

time.sleep(2)

driver.quit()