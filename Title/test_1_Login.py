import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("passingDriver")
class Test_log:

    def isElementExist(self, LocatorType, Locator):
        Element = None
        try:
            Element = self.driver.find_element(LocatorType, Locator)
            if Element:
                print("Element found")
            else:
                print("Element not found")
        except:
            print("Element not found")
        return Element


    def test_pageTitle(self):
        baseURL = "https://baseedu.in/"
        self.driver.maximize_window()
        self.driver.get(baseURL)
        pageTitle = self.driver.title
        assert self.driver.title == pageTitle

    def test_scrollDown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_clickCareers(self):
        try:
            if self.isElementExist(By.LINK_TEXT, "Careers"):
                self.driver.find_element(By.LINK_TEXT, 'Careers').click()
        except:
            print("Failed")
