# Locators:
# _usernameLogin_field = "login-user-control"
# _nextbtn_button = "btn"
# _passwordLogin_field = "login-password-control"
# _dropdownIcon_dropdown = "ui-dropdown-trigger-icon"
# _selectSite_dropdown = "//span[text()='AC1']"
# _loginbtn_button = "//button[text()='Log In']"
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tcqa/account/login")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("login-user-control").send_keys("user1")
time.sleep(3)
driver.find_element_by_xpath("//input[@type='button']").click()
time.sleep(2)
driver.find_element_by_id("login-password-control").send_keys("12345")
time.sleep(2)
driver.find_element_by_class_name("ui-dropdown-trigger-icon").click()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='AC1']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='Log In']").click()
time.sleep(3)
ele = driver.find_element_by_xpath("//a[text()='Trial Subject ']//parent::li//following-sibling::li[4]")
time.sleep(3)





