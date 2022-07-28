import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from testBase import seleniumDriver


class loginPage(seleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators:
    _usernameLogin_field = "input[id='login-user-control']"
    _nextbtn_button = "btn"
    _passwordLogin_field = "input[id='login-password-control']"
    _dropdownIcon_dropdown = "ui-dropdown-trigger-icon"
    _selectSite_dropdown = "//span[text()='AC1']"
    _loginbtn_button = "//button[text()='Log In']"
    _advancebtn = "details-button"
    _studyDropDown = "//span[contains(@class,'pi-caret-down')]"
    _study = "//ul[@id='pr_id_1_list']//span[text()='{0}']"

    def getUsernameLoginField(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._usernameLogin_field)

    def getNextbtn_button(self):
        return self.driver.find_element(By.CLASS_NAME, self._nextbtn_button)

    def getPasswordLogin(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._passwordLogin_field)

    def getDropdownIcon(self):
        return self.driver.find_element(By.CLASS_NAME, self._dropdownIcon_dropdown)

    def getSelectSite(self):
        return self.driver.find_element(By.XPATH, self._selectSite_dropdown)

    def getLoginbtn(self):
        return self.driver.find_element(By.XPATH, self._loginbtn_button)

    def getAdvancebtn(self):
        return self.driver.find_element(By.ID, self._advancebtn)

    def enterUsernameLoginField(self, username):
        self.getUsernameLoginField().send_keys(username)
        print("Username entered")

    def clickNextbtn(self):
        self.getNextbtn_button().click()

    def clickPasswordLogin(self, password):
        self.getPasswordLogin().send_keys(password)

    def clickdropdownIcon(self):
        self.getDropdownIcon().click()

    def clickSelectSite(self):
        self.getSelectSite().click()

    def clickLoginbtn(self):
        self.getLoginbtn().click()

    def clickAdvancebtn(self):
        self.getAdvancebtn().click()

    def clickStudyDropDown(self):
        return self.driver.find_element(By.XPATH, self._studyDropDown).click()

    def selectStudy(self, study):
        return self.driver.find_element(By.XPATH, self._study.format(study)).click()

    def verifyPageTitle(self):
        if "TrialComplete" in self.getPageTitle():
            return True
        else:
            return False

    def login(self, username, password):

        # try:
        #     if self.getAdvancebtn() is not None:
        #         self.clickAdvancebtn()
        #         self.driver.find_element(By.LINK_TEXT, "Proceed to tcqa (unsafe)").click()
        # except:
        #     print("No privacy window")
        #
        # waitExp = seleniumDriver(self.driver)
        # waitExp.waitExplicit(self._usernameLogin_field, "id")

        #time.sleep(3)
        self.enterUsernameLoginField(username)
        self.clickNextbtn()
        # self.waitExplicit("input[id='login-password-control']", "css")
        self.waitExplicit(self._passwordLogin_field, "css")
        self.clickPasswordLogin(password)
        self.clickdropdownIcon()
        self.clickSelectSite()
        self.clickLoginbtn()



