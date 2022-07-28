import json
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

baseURL2 = "https://tcqa/app/trialsubject/subjectidentity/identityinfo/847"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(baseURL2)
resp7 = requests.get(baseURL2)
# print(resp7)


# file = open('C:\\Auto\\API\\Post1.json', 'r')
# json_input = file.read()
# request_Json = json.loads(json_input)
# posted = requests.post(baseURL2, request_Json)
# # print(posted)
# # print(posted.text)
# print(posted.content)
# assert posted.status_code == 201