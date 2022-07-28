import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    opt = Options()
    opt.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.maximize_window()
    # driver.implicitly_wait(3)
    baseURL = "https://tcqa/account/login"
    driver.get(baseURL)
    time.sleep(10)

    print("This is one time setup")

    # request.method.driver = driver
    request.cls.driver = driver

    yield driver
    driver.close()


