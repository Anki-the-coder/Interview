import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from typing import List
from webdriver_manager.chrome import ChromeDriverManager

s = "Ankush Channe Tester"
s = s.split()
l = []
s1 = " "
for i in s:
    l.append(i)

l = l[::-1]
s1 = ' '.join(reversed(s))
# print(s1)

# Python program to convert a list
# to string using list comprehension

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])
# print(listToStr)


l2 = ' '.join(str(e) for e in s)

# print(l2)

# for i in range(25)[13:20]:
#     print(i)


x = (1, 4, 'l', 'o', 'pop', 'doll', 'pop', 'x')
# print(type(x))
# print(x.count('pop'))

y = {1, 2, 'l', 'o', 'pop', 'doll', 'y'}
# print(type(y))

my_list = [12, 65, 54, 39, 102, 339, 221, 130]
result = []
for i in my_list:
    if i % 13 == 0:
        result.append(i)
# print(result)

result1 = list(filter(lambda x1: (x1 % 13 == 0), my_list))
# print(result1)

# no = int(input("enter no "))
# power = int(input("enter power "))
# res = 1
# while power > 0:
#     res = res * no
#     power = power - 1
# print(res)

lw = [2, 12, 13, 12, 14, 12, 15, 14, 2, 10]
lw1 = [21, 121, 131, 121, 141, 121, 151, 141, 21, 101]
d = {}
for i in lw:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# element = driver.execute_script("window.scrollTo(0,y)")

d1 = {}
for i in lw:
    for j in lw1:
        d1[i] = j
        lw1.remove(j)
        break

lw2 = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
d2 = {}
for i in range(2, 11):
    # d[i] = List[filter(lambda z: z % i == 0, lw2)]
    l1 = []
    for j in lw2:
        if j % i == 0:
            l1.append(j)
    d2[i] = l1
# print(d2)

sl = ['hi', 'me', 'too']
stree = ' '.join(sl)
# print(stree)

t2 = {2, 2, 3, 'a'}
# print(type(t2))

str1 = "12abc20yz68"
temp = "0"
sm1 = 0
for i in str1:
    if i.isdigit():
        temp += i
    else:
        sm1 += int(temp)
        temp = "0"
sm2 = sm1 + int(temp)
# print(sm2)
sm3 = sum(map(int, re.findall('\d-', str1)))
# print(sm3)

stree2 = "doldol"
a = 1
for i in stree2:
    for j in range(a, len(stree2)):
        if i == stree2[j]:
            break
    else:
        # print(i)
        break
    a += 1

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
print([[x, weekdays.count(x)] for x in list(weekdays)])


s = "abcd"
# s1 = ABbCccDddd
s1 = ""
n = 1
for i in s:
    s1 += i.capitalize()
    for j in range(1, n):
        s1 += i.lower()
    n += 1
    if n <= len(s):
        s1 += "-"
print(s1)
