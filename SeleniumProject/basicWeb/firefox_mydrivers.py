from selenium import webdriver
import os


class open_browser:

    def open_firefox(self):
        # driver = webdriver.Firefox(executable_path="C:\\Users\\channank\\python\\drivers\\geckodriver.exe")

        driver = webdriver.Firefox()
        driver.get("http:\\www.lenskart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//a[contains(text(),'Shop Eyeglasses')]").click()
        driver.close()

    def open_Chrome(self):
        # driverLocation = "C:\\Users\\channank\\python\\drivers\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)

        driver = webdriver.Chrome()
        driver.get("http:\\www.lenskart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//a[contains(text(),'Shop Eyeglasses')]").click()
        driver.close()

    def open_ie(self):
        # driverLocation = "C:\\Users\\channank\\python\\drivers\\IEDriverServer.exe"
        # os.environ["webdriver.ie.driver"] = driverLocation
        # driver = webdriver.Ie(driverLocation)

        driver = webdriver.Ie()
        driver.get("http:\\www.lenskart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//a[contains(text(),'Shop Eyeglasses')]").click()
        driver.close()


test = open_browser()
test.open_firefox()
test.open_Chrome()
test.open_ie()