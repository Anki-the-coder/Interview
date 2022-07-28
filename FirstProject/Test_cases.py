import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from testRef import loginPage
from testBase import seleniumDriver
import pytest
from testStatus import statusTest
from datetime import date, timedelta


@pytest.mark.usefixtures("oneTimeSetUp")
class loginClass(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = loginPage(self.driver)
        self.seleniumMethods = seleniumDriver(self.driver)
        self.testState = statusTest(self.driver)

    def test_login(self):
        self.abc.login("user1", "789")
        self.seleniumMethods.waitExplicit("//a[text()='Trial Subject ']", "xpath")
        result1 = self.abc.verifyPageTitle()
        self.testState.mark(result1, "test_login result 1")
        self.abc.clickStudyDropDown()
        self.abc.selectStudy("Jupiter")
        result2 = self.seleniumMethods.isElementPresent("//a[text()='Trial Subject ']", "xpath")
        self.testState.markFinal("test_login", result2, "test_login result 2")

    # def test_searchNavigation(self):
    #     trialSubject = self.driver.find_element(By.XPATH, "//a[text()='Trial Subject ']").click()
    #     subjectProcess = self.driver.find_element(By.XPATH, "//span[text()='Subject Process']").click()
    #     subjectSearch = self.driver.find_element(By.XPATH, "//a[text()=' Subject Search ']").click()
    #     # added code for subject addition
    #     plusIcon = self.driver.find_element(By.XPATH, "//span[contains(@class,'imed-icon-plus')]").click()
    #     name = round(time.time()*1000)
    #     dt = date.today() - timedelta(5)
    #     firstName = self.driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']").send_keys(dt)
    #     lastName = self.driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']").send_keys(name)
    #     genderList = self.driver.find_element(By.CSS_SELECTOR, "[id='r_id_13_list']")
    #     gender = random.choice(genderList)
    #     self.driver.sleep(5)

    # def test_searchDialogInIdentifier(self):
    #     trialSubject = self.driver.find_element(By.XPATH, "//a[text()='Trial Subject ']").click()
    #     subjectIdentity = self.driver.find_element(By.XPATH, "//span[text()='Subject Identity']").click()
    #     moreLink = self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']/a").click()

    # def test_createSubject(self):
    #     time.sleep(3)
    #     self.seleniumMethods.waitExplicit("//a[text()='Trial Subject ']", "xpath")
    #     trialSubject = self.driver.find_element(By.XPATH, "//a[text()='Trial Subject ']").click()
    #     subjectIdentity = self.driver.find_element(By.XPATH, "//span[text()='Subject Identity']").click()
    #     time.sleep(3)
    #     self.seleniumMethods.waitExplicit("//span[contains(@class,'imed-icon-plus')]", "xpath")
    #     plusIcon = self.driver.find_element(By.XPATH, "//span[contains(@class,'imed-icon-plus')]").click()
    #     name = round(time.time()*1000)
    #     dt = date.today() - timedelta(5)
    #     firstName = self.driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']").send_keys(dt)
    #     lastName = self.driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']").send_keys(name)
    #     genderList = self.driver.find_element(By.CSS_SELECTOR, "[id='r_id_13_list']")
    #     gender = random.choice(genderList)
    #     time.sleep(3)

    # @pytest.mark.run(order=4)
    # def test_searchDialogInMedical(self):
    #     trialSubject = self.driver.find_element(By.XPATH, "//a[text()='Trial Subject ']").click()
    #     subjectProcess = self.driver.find_element(By.XPATH, "//span[text()='Subject Medical']").click()
    #     moreLink = self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']/a").click()
    #
    # @pytest.mark.run(order=5)
    # def test_searchDialogInLabReview(self):
    #     trialLab = self.driver.find_element(By.XPATH, "//a[text()='Trial Lab ']").click()
    #     resultReview = self.driver.find_element(By.XPATH, "//span[text()='Result Review']").click()
    #     moreLink = self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']/a").click()
    #
    # # @pytest.mark.usefixtures("reduceBrowser")
    # # @pytest.mark.run(order=3)
    # @pytest.mark.trylast()
    # def test_createContainers(self):
    #     # trialLab = self.driver.find_element(By.XPATH, "//span[@class='imed-icon imed-icon-tlab']").click()
    #     trialLab = self.driver.find_element(By.LINK_TEXT, "Trial Lab ").click()
    #     libraries = self.driver.find_element(By.XPATH, "//div[@data-target='#10']//span[text()='Libraries']").click()
    #     containers = self.driver.find_element(By.XPATH, "//a[text()='Containers']").click()

