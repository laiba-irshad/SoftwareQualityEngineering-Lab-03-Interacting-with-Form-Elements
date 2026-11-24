from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open registration form
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# Select Male
male = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
male.click()
time.sleep(2)

# Verify Male selection
male_radio = driver.find_element(By.ID, "gender-radio-1")
print("Male Selected:", male_radio.is_selected())

# Select Female
female = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
female.click()
time.sleep(2)

# Verify Female selection
female_radio = driver.find_element(By.ID, "gender-radio-2")
print("Female Selected:", female_radio.is_selected())

# Verify Male is no longer selected
print("Male Selected After Female:", male_radio.is_selected())

driver.quit()