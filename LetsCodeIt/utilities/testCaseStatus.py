from base.testSeleniumDrivers import seleniumDrivers
import utilities.customLogger as customLog
import logging


class testCaseStatus(seleniumDrivers):

    log = customLog.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.resultList = []

    def testResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("Pass")
                else:
                    self.resultList.append("Fail")
                    self.takeScreenshot(resultMessage)
            else:
                self.resultList.append("Fail")
                self.takeScreenshot(resultMessage)
        except:
            self.resultList.append("Some Exception occurred")
            self.takeScreenshot(resultMessage)

    def testMark(self, result, resultMessage):
        self.testResult(result, resultMessage)

    def testMarkFinal(self, testName, result, resultMessage):
        self.testResult(result, resultMessage)

        if "Fail" in self.resultList:
            self.log.info(testName + ": test case Failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + ": test case Passed")
            self.resultList.clear()
            assert True == True
