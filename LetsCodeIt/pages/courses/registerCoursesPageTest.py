from base.testBasePage import baseClass
import utilities.customLogger as customLog
import logging


class coursesPageTest(baseClass):

    log = customLog.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _loginButton1 = "//a[contains(text(),'Login')]"
    _loginEmail = "user_email"
    _loginPassword = "user_password"
    _loginButton2 = "commit"
    _searchCourseField = "search-courses"
    _searchCourseButton = "search-course-button"
    _javaScriptCourse = "//div[contains(text(),'JavaScript for beginners')]"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enrollButton = "//button[@id='enroll-button-top']"
    _cardNumber = "cardnumber"
    _expDate = "exp-date"
    _cvc = "cvc"
    _agreeTerms = "agreed_to_terms_checkbox"

    # Get elements
    def getLoginButton1(self):
        return self.getElement(self._loginButton1, "xpath")

    def getLoginEmail(self):
        return self.getElement(self._loginEmail, "id")

    def getLoginPassword(self):
        return self.getElement(self._loginPassword, "id")

    def getLoginButton2(self):
        return self.getElement(self._loginButton2, "name")

    def getSearchCourseField(self):
        return self.getElement(self._searchCourseField, "id")

    def getSearchCourseButton(self):
        return self.getElement(self._searchCourseButton, "id")

    def getJavaCourse(self):
        return self.getElement(self._javaScriptCourse, "xpath")

    def getCourse(self, courseName):
        return self.getElement(self._course.format(courseName), "xpath")

    def getEnrollButton(self):
        return self.getElement(self._enrollButton, "xpath")

    def getCardNumber(self):
        return self.getElement(self._cardNumber, "name")

    def getExpDate(self):
        return self.getElement(self._expDate, "name")

    def getCVC(self):
        return self.getElement(self._cvc, "name")

    def getAgreeTerms(self):
        return self.getElement(self._agreeTerms, "id")

    # Perform actions on element
    def clickLoginButton1(self):
        self.getLoginButton1().click()

    def enterLoginEmail(self, email):
        self.waitExplicit(self._loginEmail, "id")
        self.getLoginEmail().send_keys(email)

    def enterLoginPassword(self, password):
        self.getLoginPassword().send_keys(password)

    def clickLoginButton2(self):
        self.getLoginButton2().click()

    def enterSearchCourseField(self, course):
        self.getSearchCourseField().send_keys(course)

    def clickSearchCourseButton(self):
        self.getSearchCourseButton().click()

    def clickCourse(self, courseName):
        self.getCourse(courseName).click()

    def clickEnrollButton(self):
        self.waitExplicit(self._enrollButton, "xpath")
        self.getEnrollButton().click()

    def enterCardNumber(self, cardNumber):
        self.driver.switch_to.frame("__privateStripeFrame8")
        self.getCardNumber().clear()
        self.getCardNumber().send_keys(cardNumber)
        self.driver.switch_to.parent_frame()

    def enterExpDate(self, ExpDate):
        self.driver.switch_to.frame("__privateStripeFrame9")
        self.getExpDate().clear()
        self.getExpDate().send_keys(ExpDate)
        self.driver.switch_to.parent_frame()

    def enterCVC(self, CVC):
        self.driver.switch_to.frame("__privateStripeFrame10")
        self.getCVC().send_keys(CVC)
        self.driver.switch_to.parent_frame()

    def clickAgreeTerms(self):
        self.getAgreeTerms().click()

    def verifyLogin(self):
        result = self.isElementPresent(self._searchCourseField, "id")
        return result

    def verifyPurchaseCourse(self):
        result = self.isElementPresent(self._agreeTerms, "id")
        return result
