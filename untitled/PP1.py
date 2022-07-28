import random
import time


def pwd():
    strength = input("Select your pwd strength: weak, mid, strong: ")
    weakpwd = ['mon', 'tue', 'wed', 'thus']

    if strength == 'weak':
        print("Your new pwd is: ", random.choice(weakpwd))
    elif strength == 'mid':
        print("Your new pwd is: ", )


# x = []
# for i in range(1, 4):
#     a = int(input("Enter the " + str(i) + " no.: "))
#     x.append(a)
# x.sort()

# d = {'a': 12, 'b': 15, 'c': 21}
# name = input("Enter the name: ")
# print(d[name])

# e = {}
# n = int(input("Enter the length of dict: "))
# for k in range(n):
#     a = input("Enter the key: ")
#     b = input("Enter the value: ")
#     e[a] = b
#
# print(e)

# z = {'ab': '12', 'cd': '34', 'ef': '56', 'gh': '78'}
# y = {}
# for key, value in z.items():
#     z[value] = key
#
# x = {value: key for key, value in z.items()}
# print(x)

# emp_dict = {
#     "company": {
#         "employee": {
#             "name": "Jess",
#             "payable": {
#                 "salary": 9000,
#                 "increment": 12
#             }
#         }
#     }
# }
#
# print(emp_dict['company']['employee']['payable']['increment'])


# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# list1[1][2][2][1] = 3500
# print(list1)


# def outer(xy, yz):
#     def inner1():
#         return xy + yz
#
#     return inner1() + 'developer'
#
# k = outer('Emma', 'Kelly')
# print(k)

# y = 5
# count = 0
# for i in range(y):
#     count += 1
#     for j in range(0, i + 1):
#         print(count, end=" ")
#     print('\r')
#
