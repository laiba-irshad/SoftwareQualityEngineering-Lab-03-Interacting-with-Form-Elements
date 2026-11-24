from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# Open dropdown demo page
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

# Locate dropdown
dropdown_element = driver.find_element(By.ID, "dropdown")

# Create Select object
dropdown = Select(dropdown_element)

# Select by visible text
dropdown.select_by_visible_text("Option 1")
print("Selected by Text:", dropdown.first_selected_option.text)

time.sleep(2)

# Select by index
dropdown.select_by_index(2)
print("Selected by Index:", dropdown.first_selected_option.text)

time.sleep(2)

# Select by value
dropdown.select_by_value("1")
print("Selected by Value:", dropdown.first_selected_option.text)

time.sleep(2)

driver.quit()