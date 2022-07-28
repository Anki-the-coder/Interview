from selenium import webdriver
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="class")
def getDriver(request):
    baseURL = "https://letskodeit.teachable.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)
    driver.implicitly_wait(3)
    request.cls.driver = driver
    
    yield driver
    driver.close()
