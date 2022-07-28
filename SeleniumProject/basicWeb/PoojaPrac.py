from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://semantic-ui.com/modules/dropdown.html")

driver.execute_script("window.scrollBy(0,1200);")

driver.find_element_by_xpath("//div[@class='ui fluid dropdown selection multiple']").click()
# driver.find_element_by_xpath("//div[contains(@class,'ui fluid dropdown selection multiple')]//div[text()='CSS']").click()
# driver.find_element_by_xpath("//div[contains(@class,'ui fluid dropdown selection multiple')]//div[text()='HTML']").click()

# ele = driver.find_element_by_xpath("//div[contains(@class,'ui fluid dropdown selection multiple')]//div[@class='item']")
elements = driver.find_elements_by_xpath("//div[contains(@class,'ui fluid dropdown selection multiple')]//div[@class='item']")

# webdriver.

for e in elements:
    if e.text != 'CSS':
        print(e.text)
        e.click()








# #sel.select_by_value("angular")

# driver.get("https://letskodeit.teachable.com/courses")
# driver.find_element_by_xpath("//a[@class='fedora-navbar-link navbar-link']").click()
# driver.implicitly_wait(20)
# s=Select(driver.find_element_by_id("multiple-select-example"))
# s.select_by_value("apple")
# s.select_by_index(1)
# s.deselect_all()
#
# car = Select(driver.find_element_by_id("carselect"))
# car.select_by_value("benz")
