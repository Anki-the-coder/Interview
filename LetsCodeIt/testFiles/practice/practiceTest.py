import time
from pages.courses.registerCoursesPageTest import coursesPageTest
from pages.practice.practicePage import practicePage
import unittest
import utilities.customLogger as customLog
import logging
import pytest
from utilities.testCaseStatus import testCaseStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("getDriver")
@ddt
class practiceTest(unittest.TestCase):

    log = customLog.customLogger(logLevel=logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, getDriver):
        self.practicePage = practicePage(self.driver)
        self.coursesPage = coursesPageTest(self.driver)
        self.testCaseStatus = testCaseStatus(self.driver)

    # def test_login(self):
    #     self.coursesPage.clickLoginButton1()
    #     time.sleep(10)
    #     self.coursesPage.enterLoginEmail("test@email.com")
    #     self.coursesPage.enterLoginPassword("abcabc")
    #     self.coursesPage.clickLoginButton2()
    #     result = self.coursesPage.verifyLogin()
    #     self.testCaseStatus.testMarkFinal("test_login", result, "Result of test_login")

    @data("bmw", "benz", "peach", "bmw")
    @unpack
    def test_performAction(self, radioOption, dropDownOption, multiSelectOption, checkBoxOption):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        self.practicePage.clickRadioButton(radioOption)
        self.practicePage.clickDropDown(dropDownOption)
        self.practicePage.clickMultiSelect(multiSelectOption)
        self.practicePage.clickCheckBox(checkBoxOption)

