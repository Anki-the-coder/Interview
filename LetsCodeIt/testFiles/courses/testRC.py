import unittest
import pytest
from pages.courses.registerCoursesPageTest import coursesPageTest
from utilities.testCaseStatus import testCaseStatus
import utilities.customLogger as customLog
import logging
from ddt import ddt, data, unpack
import time
from utilities.readData import getReadData


@pytest.mark.usefixtures("getDriver")
@ddt
class buyCourseTest(unittest.TestCase):

    log = customLog.customLogger(logLevel=logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, getDriver):
        self.coursesPage = coursesPageTest(self.driver)
        self.testCaseStatus = testCaseStatus(self.driver)

    def test_login(self):
        self.coursesPage.clickLoginButton1()
        time.sleep(10)
        self.coursesPage.enterLoginEmail("test@email.com")
        self.coursesPage.enterLoginPassword("abcabc")
        self.coursesPage.clickLoginButton2()
        result = self.coursesPage.verifyLogin()
        self.testCaseStatus.testMarkFinal("test_login", result, "Result of test_login")

    # @data(*getReadData("C:\\Auto\\PycharmProjects\\LetsCodeIt\\testData.csv"))
    @data(["JavaScript", " 9999888877776666", "0824", "786"], ["Selenium WebDriver With Java", " 8888777766669999",
                                                               "622", "420"], ["Mac Linux Command Line Basics",
                                                                               " 7777666655554444", "1030", "111"])
    @unpack
    def test_purchaseCourse(self, courseName, cardNum, cardExp, cardCVV):
        self.coursesPage.enterSearchCourseField(courseName)
        self.coursesPage.clickSearchCourseButton()
        self.coursesPage.clickCourse(courseName)
        self.coursesPage.clickEnrollButton()
        self.coursesPage.enterCardNumber(cardNum)
        self.coursesPage.enterExpDate(cardExp)
        self.coursesPage.enterCVC(cardCVV)
        self.coursesPage.clickAgreeTerms()
        result = self.coursesPage.verifyPurchaseCourse()
        self.testCaseStatus.testMarkFinal("test_purchaseCourse", result, "Result of test_login Purchase course")
        self.driver.get("https://letskodeit.teachable.com/courses")
