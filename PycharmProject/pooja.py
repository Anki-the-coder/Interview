# import datetime

import json
import requests

baseURL = "https://www.facebook.com/friends/?profile_id=100054354240642"

resp1 = requests.get(baseURL)
# print(resp1.content)

resp2 = requests.head(baseURL)
# print(resp2.content)

resp3 = requests.options(baseURL)
print(resp3.)





# dict1 = '{"k1":"val1","k2":"val2"}'
# result = json.loads(dict1)
# print(result['k1'])

#
# d = datetime.datetime.now()
#
# print(d.strftime("%d-%m-%Y %H:%M:%S"))
#
# import sys
#
# print(sys.version)
# print(sys.version_info)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com/")
# driver.implicitly_wait(3)
# driver.find_element_by_class_name("gLFyf").send_keys("selenium")
#
# element = driver.find_elements(By.XPATH, "//ul//li[@class='sbct']//div[@class='sbl1']/span")
# print(len(element))
#
# for e in element:
#     print("*/")
#     print(e.text)
#
# driver.get("https://www.facebook.com")
# _email = driver.find_element_by_id("email").send_keys("my_account")
# _pwd = driver.find_element_by_id("pass").send_keys("my_pwd")
#
# try:
#     _eye = WebDriverWait(driver, 3).until(
#         # EC.element_to_be_clickable((By.XPATH, "//div[@class='_9lsb _9ls8']"))
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "div._9lsb._9ls8"))
#     )
#     _eye.click()
#     print("Dunzo Buoy")
#     driver.quit()
# except:
#     print("No Exception found")
#     driver.quit()
