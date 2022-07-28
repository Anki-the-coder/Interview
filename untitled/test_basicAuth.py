import json
import requests
import jsonpath
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_demoURL():
    demo_url = "https://epdemo/app/trialsubject/subjectidentity/identityinfo/248"
    demo_new_user = "https://epdemo/app/trialsubject/subjectidentity/identityinfo/New"

    # opt = Options()
    # opt.add_argument("--ignore-certificate-errors")
    # opt.add_argument("--headless")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    # driver.get(demo_url)

    # get_demo_url = requests.get(demo_url, verify=False)
    get_demo_url = requests.get(demo_url, auth=HTTPBasicAuth('user1', '789'))
    # print(get_demo_url.content)

    get_demo_new_user = requests.get(demo_new_user, verify=False)
    print(get_demo_new_user.text)
    put_file = open("C:\\Auto\\API\\tc1.json", "r")
    read_put_file = json.loads(put_file.read())
    put_data = requests.post(demo_new_user, read_put_file)
    print(put_data.text)

