from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open checkbox demo page
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)

# Locate first checkbox
checkbox = driver.find_element(By.XPATH, "//input[1]")

# Check initial state
initial_state = checkbox.is_selected()
print("Initial State:", initial_state)

# Click checkbox
checkbox.click()
time.sleep(2)

# Check new state
new_state = checkbox.is_selected()
print("After First Click:", new_state)

# Click checkbox again
checkbox.click()
time.sleep(2)

# Check final state
final_state = checkbox.is_selected()
print("After Second Click:", final_state)

driver.quit()