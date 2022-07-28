# import math
# from math import pi
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
# import logging
import unittest


class area:

    def area_circle(self):
        rad = float(input("Enter the radius: "))
        areacircle = pi * rad ** 2
        print("Area of the circle is: " + str(areacircle))

    def staticarea(self, r):
        areacircle = pi * r ** 2
        print("Area of the circle is: " + str(areacircle))


result = area()


# result.area_circle()
# result.staticarea(20)


class string_manupulation(area):

    def ulta(self):
        name = input("Enter your good name: ")
        lastname = input("Enter you last name: ")
        fullname = name + ' ' + lastname
        print("Your full name is: " + fullname)
        print("Your full name in reverse order is: ")
        print(fullname[::-1])


manu = string_manupulation()


# manu.ulta()
# manu.area_circle()


# org = input("Please enter your numbers: ")
# list123 = org.split(",")
# print(list123)


# first = input("Enter the no")
# second = first
# third = second.join(first)

# total = int(first + second)
# print(total)

# # num = int(input("Enter the no"))
#
# if num < 17:
#     print(17-num)
# else:
#     print((num-17)*2)


# a = input("Enter your string now: ")
# print(a[:2])
# # a.lower()
# # print(b)
#
# if a.startswith("is"):
#     print(a)
# else:
#     print("Is " + a)


# num = int(input("number please"))
#
# if num % 2:
#     print("Odd")
# else:
#     print("even")

#
# org = input("Enter the no in the list")
# a_list = org.split(",")
# print(a_list)
# # print(a_list.count('4'))

a_list = ['1', '2', '3', '4']
for z in a_list:
    print("@ " * int(z))

for z in a_list[2::-1]:
    print("@ " * int(z))

# a = 10
# for i in range(11):
# print("# " * int(i))

# for i in range(11, 0, -1):
#     print('$ ' * int(i))


class runInChrome:

    def searchingInChrome(self):
        driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://www.google.com")
        searchBox = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
        searchBox.click()
        # searchBox.send_keys("Selenium")
        # searchBox.submit()
        # driver.find_element(By.XPATH, "//h3[@class='LC20lb DKV0Md']").click()

        searchBox.send_keys("amazon")
        searchBox.submit()
        driver.find_element(By.XPATH, "//h3[@class='LC20lb DKV0Md']").click()
        driver.find_element_by_id("a-autoid-0-announce").click()
        driver.find_element_by_id("ap_email").click()
        driver.find_element_by_id("ap_email").send_keys("9890136577")
        driver.find_element_by_id("continue").click()
        driver.find_element_by_id("ap_password").send_keys("fBVhik2x")
        driver.find_element_by_id("signInSubmit").click()
        driver.find_element(By.XPATH, "// a[contains(text(), 'Mobiles')]").click()


# sea = runInChrome()
# sea.searchingInChrome()

class MyTrip:

    def makeMyTrip(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://www.google.com")
        driver.implicitly_wait(10)
        searchBox = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
        searchBox.click()
        searchBox.send_keys("makeMyTrip")
        searchBox.submit()
        driver.find_element(By.XPATH, "//h3[@class='LC20lb DKV0Md']").click()

        time.sleep(5)

        # destinationFileName = "C:\\Users\\channank\\Desktop\\Screenshots\ScreenshotCaptured.png"
        driver.save_screenshot("C:\\Users\\channank\\Desktop\\Screenshots\ScreenshotCaptured1.png")

        driver.find_element(By.XPATH,
                            "//a[@id='webklipper-publisher-widget-container-notification-close-div'/i]").click()

        driver.implicitly_wait(10)

        driver.find_element(By.ID, "fromCity").click()

        # driver.find_element(By.ID, "fromCity").send_keys("Pune")
        # driver.find_element_by_xpath(//input[@placeholder='From']).send_keys("Pune")
        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("Pune")
        driver.find_element(By.XPATH, "//p[contains(text(), 'Pune, India')]").click()

        driver.find_element(By.ID, "webklipper-publisher-widget-container-notification-close-div").click()

        driver.find_element(By.ID, "toCity").click()
        # driver.find_element(By.ID, "toCity").send_keys("Hyderabad")
        driver.find_element_by_xpath('//input[@placeholder="To"]').send_keys("Hyderabad")
        driver.find_element_by_xpath("//p[contains(text(), 'Hyderabad, India')]").click()

        driver.find_element_by_xpath('//input[@placeholder="To"]').submit()

        driver.find_element_by_id("departure").click()
        driver.find_element(By.CLASS_NAME, "DayPicker-NavButton--next").click()


trip = MyTrip()
# trip.makeMyTrip()

#
myList = ['This', 'is', 'a', 'list']
sentence = myList[0]

for word in myList[1:]:
    sentence = sentence + ' ' + word

# print(sentence)
#
# print(" ".join(myList))


a = 'THIs IS A STRING'
# a = 'this is a string'

small = a.islower()


# if any(small) == True:
#     print("Lower")
# else:
#     print("Upper")

# if a is not a.isupper():
#     print("lower")
# else:
#     print("Upper")


# d1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# d1 = {'k1': 'v1'}
#
# c1 = d1.items()
#
# print(c1)
# print(c2)


# logging.basicConfig(filename="log1.log", level=logging.INFO)
# logging.basicConfig(filename="test.log", level=logging.DEBUG)

# logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%d/%m/%Y %I:%M:%S %p',
#                     level=logging.INFO)
#
#
# logging.debug("Debug msg")
# logging.info("Info msg")
# logging.critical("Critical msg")


class testingThis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("I am a setup method")

    def setUp(self):
        print("I am setup")

    def test_print1(self):
        print("This is print 1")

    def test_print2(self):
        print("This is print 2")

    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print("I am tear down class")


if __name__ == '__main__':
    unittest.main(verbosity=2)
