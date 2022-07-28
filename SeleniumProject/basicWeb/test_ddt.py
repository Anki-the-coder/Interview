import time
from SeleniumProject.basicWeb.XLUtils import XlUtils
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(4)

driver.get("http://demo.guru99.com/test/newtours/")

xl = XlUtils()

path = "C:\\Auto\\PycharmProjects\\SeleniumProject\\basicWeb\\ddt.xlsx"

col = xl.get_colCnt(path, "data")
row = xl.get_rowCnt(path, "data")
# value = xl.read_rows(path, "data",2,1)
# data = xl.write_to_column(path, "data",2,1,"pk")

print(col)
print(row)
# print(value)
# print(data)


for i in range(2, row + 1):
    driver.find_element(By.LINK_TEXT, "Home").click()

    username = driver.find_element(By.XPATH, "//input[@name='userName']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    login = driver.find_element(By.NAME, "submit")

    uname = xl.read_rows(path, "data", i, 1)
    pswrd = xl.read_rows(path, "data", i, 2)

    # username.click()
    username.send_keys(uname)
    print(uname)
    # password.click()
    password.send_keys(pswrd)
    print(pswrd)

    login.click()

    try:
        assert driver.find_element(By.XPATH, "//h3")
        xl.write_to_column(path, "data", i, 3, "pass")
    except:
        xl.write_to_column(path, "data", i, 3, "fail")


driver.close()
