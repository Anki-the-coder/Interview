from traceback import print_stack
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
import utilities.customLogger as customLog
import logging


class seleniumDrivers:

    log = customLog.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                  " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                  " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                  " and locatorType: " + locatorType)
        return element

    def isElementPresent(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        if element:
            return True
        else:
            return False

    def takeScreenshot(self, resultMessage):
        fileName = resultMessage + "_" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\Screenshots\\"
        relativePath = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativePath)
        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot captured at the location: " + destinationFolder)
        except:
            self.log.info("Screenshot not captured")
            print_stack()

    def waitExplicit(self, locator, locatorType='id', timeout=10, poll_frequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType, locator)))
            self.log.info("Using explicit wait function for element: " + str(element))
            self.log.info("Clicked on element " + str(element))
        except:
            self.log.info("Element not found " + str(element))
            print_stack()
        return element
