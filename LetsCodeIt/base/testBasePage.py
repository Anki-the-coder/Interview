from base.testSeleniumDrivers import seleniumDrivers


class baseClass(seleniumDrivers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
