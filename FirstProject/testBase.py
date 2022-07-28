from traceback import print_stack
import pytest
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from testUtility import customLog
import time
import os
from selenium import webdriver


class seleniumDriver:
    log = customLog()

    def __init__(self, driver):
        self.driver = driver

    @pytest.fixture(scope="module")
    def reduceBrowser(self):
        self.driver.execute_script("document.body.style.zoom='75%'")

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'parlinktext':
            return By.PARTIAL_LINK_TEXT
        elif locatorType == 'tagname':
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locatorType + "is not valid")
            return False

    def waitExplicit(self, locator, locatorType='id', timeout=10, poll_frequency=0.5):
        element = None
        try:
            baseType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
            element = wait.until(ec.element_to_be_clickable((baseType, locator)))
            self.log.info("using explicit wait function")
            self.log.info("Clicked on element " + str(element))
        except:
            self.log.info("Element not found " + str(element))
            print_stack()
        return element

    def isElementPresent(self, locator, locatorType='id'):
        # element = self.driver.find_element(locatorType, locator)
        element = self.getElement(locator, locatorType)
        try:
            if element is not None:
                self.log.info("Element Found " + str(element))
                return True
            else:
                self.log.info("Element not Found " + str(element))
                return False
        except:
            self.log.info("Element not Found " + str(element))
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            baseType = self.getByType(locatorType)
            element = self.driver.find_element(baseType, locator)
            self.log.info("Element Found with Locator type: " + locatorType + " and locator: " + locator)
        except:
            self.log.info("Element Not Found with Locator type: " + locatorType + " and locator: " + locator)
        return element

    def getPageTitle(self):
        return self.driver.title

    def takeScreenshot(self, resultMessage):
        fileName = resultMessage + "_" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = ".\\Screenshots\\"
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
