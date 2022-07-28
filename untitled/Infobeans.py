# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
#
#
# print(fun(data[0]))

#
#
# d1 = {1:2,  2:3}
# d2 = {3:4, 4:5}
#
# d3 = d1+d2


# class custom(BaseException):
#
#     def someError(self):
#         pass

#
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occured")
# except "someError":
#     print("someError has occured")
#
# if '1' != 1:
#     print("hi")

# list1=[1,2,3]
# list2=[1,2,3]
#
# print(list1 is list2)
#
# @[]{user: test, pwd: pwd, emila:re@.dcs},}
# def testlogin


# import pytest
#
#
# class Test_abc:
#     @pytest.mark.parametrize("n1,n2,result", [(1, 5, 3), (3, 5, 1), (4, 5, 9)])
#     def test_add(self, n1, n2, result):
#         # assert n1 + n2 == result
#         # print(n1+n2+result)
#         print(n1+n2)
# # test_add()



# 2nd round
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.remove.bg/")
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
links = driver.find_elements(By.XPATH, "//*[@href]")
print("Total links on webpage are: " + str(len(links)))
workingLinks = 0
nonWorkingLinks = 0
for link in links:
    try:
        url = link.get_attribute('href')
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            workingLinks += 1
        else:
            nonWorkingLinks += 1
    except:
        print("Some exception")

driver.close()

print("Working links are: " + str(workingLinks))
print("Non Working links are: " + str(nonWorkingLinks))
