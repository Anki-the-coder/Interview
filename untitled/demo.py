import re
import statistics

# def maxi():
#     list1 = [5, 15, 51, 35, 40]
#     max_no = list1[0]
#     for x in list1:
#         if x > max_no:
#             max_no = x
#     return max_no
# var = maxi()
# print(var)


list1 = [5, 15, 51, 35, 40, 10]
list1.sort(reverse=True)
# print(list1)


di = {list1[i]: list1[i + 1] for i in range(0, len(list1), 2)}
# print(di)


test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# print(res)


# import random
#
# ranNo = random.randint(10, 59)
# print(ranNo)
# l1 = [0]
# print(l1)
# count = 0
# while True:
#     GuessNo = int(input("Enter your value: "))
#     count += 1
#     diff = ranNo - GuessNo
#     l1.append(abs(diff))
#
#     if ranNo == int(GuessNo):
#         print("You are right!!!")
#         break
#     else:
#         # if (ranNo - 10) <= int(GuessNo) <= (ranNo + 10):
#         if GuessNo in range(ranNo - 10, ranNo + 11):
#             if count == 1:
#                 print("Warm")
#             else:
#                 if l1[-2] >= l1[-1]:
#                     print("Warmer")
#                 else:
#                     print("Colder")
#         else:
#             if count == 1:
#                 print("Cold")
#             else:
#                 if l1[-2] >= l1[-1]:
#                     print("Warmer")
#                 else:
#                     print("Colder")
#
# print("You took", count, "no. of attempts")


# no1 = int(input("Enter no1 "))
# no2 = int(input("Enter no2 "))
# for i in range(no1, no2 + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             print(i, " is not prime")
#             break
#     else:
#         print(i, " is prime")


# # Python program to print duplicates from a list of integers
# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated


# # Driver Code
# list1 = [10, 20, 30, 20, 20, 30, 40,
#          50, -20, 60, 60, -20, -20]
# print(Repeat(list1))

# This code is contributed
# by Sandeep_anand


# str1 = "geeks for geeks"
# lst = str1.split()
# d = {}
# for i in lst:
#     d[i] = lst.count(i)
#     res1 = min(d, key=d.get)
#     print(res1)
#
# res = str1.replace("_", " ").title().replace(" ", "")
# print(res)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# driver = webdriver.Chrome(ChromeDriverManager().install())
# url = 'https://www.goibibo.com/'
# driver.get(url)
# driver.maximize_window()
# loginPopup = driver.find_element(By.XPATH, "//div/button[@class='lsPop__cta']")
# time.sleep(120)
# wait = WebDriverWait(driver, 12).until(ec.visibility_of_element_located)
# if loginPopup:
#     print("It exist")
# driver.close()


# stri = input("Enter the string: ")
# li = stri.strip()
# cnt = 0
# for i in li:
#     for j in range(len(li)+1):
#         # print(i*j)
#         if cnt == j:
#             print(i * cnt)
#             cnt += 1


# x = 10
# if x >= 11:
#     y = 3
# else:
#     if x < 6:
#         y = 4
#     else:
#         y = 2
#         z = x * y + 1
#     print(z, z % 7)
#
# print('{} {} {}'.format(10, 'helo', True))

# class A :
#     def __init__(self,id):
#         self.__id = id
#         id =100
#         x=A(10)
#         print(x.id)
#
# a= A(10)

# m = [[x,y] for x in range(3) for y in range(4)]
# print('a b c d'.split())
#
# def g(a=1,b=2,c=3):
#     print("%d %d %d" %(a,b,c))
# g()

# l = ["hoi","ll"]
# z= map(lambda x : len(x),l)
# print(z)

# print(reduce(lambda  x,y : x+y*y,[2,3,5],0))

x, y = 1, 1

# def f():
#     global x
#     y=0
#     for i in (10,20,30):
#         x+=1
#         y+=1
#
# f()
# print(x,y)

# print(17/2%2*3**3)

# l =['a','p','b']
# l.sort()
# print(l)

# def f(l,in1):
#     map(lambda x : x+in1 ,l)
#
# arr = [1,2,3]
# f(arr,1)
# print(arr)
# l = [1,2,3,4,5]
# print(l[-1:1:-2])

# def f(g,*args):
#     return g(args)
# print(f(lambda z : reduce ))

# z=[[i for i in range(j,j+2)] for j in range(1,6,2)]
# print(z)

a = tuple('abcde')
a, b, c, d, e = a
b = c = '*'
a = (a, b, c, d, e)
# print(a)


# # while True print("aa")
#
# print("Content-Type: text/plain\n\n")
# print("welcone\n")

class inputText:
    def __init__(self, input_text):
        self.input_text = input_text

        def display(self):
            return self.input_text

        mynum = inputText("1234567890")
        # print(mynum.display())
