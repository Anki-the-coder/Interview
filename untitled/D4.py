import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
driver.implicitly_wait(10)
elem = "//span[@id='nav-cart-count']"
wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable, EC.visibility_of_element_located((By.XPATH, elem)))
driver.find_element_by_xpath(elem).click()
time.sleep(3)

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(handle)
driver.switch_to.default_content()
driver.switch_to.parent_frame()

driver.close()


# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((By.XPATH, "xyz")))
