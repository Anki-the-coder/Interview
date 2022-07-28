from base.testBasePage import baseClass
import utilities.customLogger as customLog
import logging


class practicePage(baseClass):
    log = customLog.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:
    _radioButton = "//div[@id='radio-btn-example']//input[@value='{0}']"
    _dropDown = "//div[@id='select-class-example']//option[@value='{0}']"
    _multiSelect = "//div[@class='cen-right-align']//option[@value='{0}']"
    _checkBox = "//div[@id='checkbox-example']//input[@value='{0}']"

    # perform actions on element
    def clickRadioButton(self, value):
        self.getElement(self._radioButton.format(value), "xpath").click()

    def clickDropDown(self, value):
        self.getElement(self._dropDown.format(value), "xpath").click()
        # self.getElement(self._dropDown.)

    def clickMultiSelect(self, *value):
        multiSelectList = []
        for val in value:
            multiSelectList.append(val)
        for item in multiSelectList:
            self.getElement(self._multiSelect.format(item), "xpath").click()

    def clickCheckBox(self, *value):
        checkBoxList = []
        for val in value:
            checkBoxList.append(val)
        for item in checkBoxList:
            self.getElement(self._checkBox.format(item), "xpath").click()
