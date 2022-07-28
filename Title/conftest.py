from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="class")
def passingDriver(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver

    yield
    driver.close()
