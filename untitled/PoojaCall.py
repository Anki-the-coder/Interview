# class addSub:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self):
#         c = self.a + self.b
#         return c
#
#     def sub(self):
#         c = self.a - self.b
#         return c
#
#
# class mulDiv(addSub):
#     def __init__(self, a, b):
#         super(mulDiv, self).__init__(a, b)
#
#     def mul(self):
#         d = self.a * self.b
#         return d
#
#     # def div(self):
#     #     try:
#     #         d = self.a / self.b
#     #         return d
#     #     except:
#     #         print("This is a Zero division exception")
#     #     else:
#     #         print("this is else statement")
#     #     finally:
#     #         print("Finally the block is executed")
#
#     def __add__(self):
#         print("class muldiv for add starts from here ...")
#         # super(mulDiv, self).__add__()
#
#     def sub(self):
#         # super(mulDiv, self).sub()
#         e = (super().sub())
#         print(e)
#         print("class muldiv for sub starts from here ...")
#
#
# class addMul(mulDiv):
#     def __init__(self, a, b):
#         super(addMul, self).__init__(a, b)
#
#     def div(self):
#         try:
#             d = self.a / self.b
#             print(d)
#
#         except:
#             print("This is a Zero division exception")
#             raise Exception("In exception")
#
#         else:
#             print("this is else statement")
#         finally:
#             print("Finally the block is executed")
#
#
# ans2 = mulDiv(20, 3)
#
# ans1 = addMul(20, 0)
# ans1.div()
#
# # print(addMul.div(d))
# # print(r)
#
#
# # ans2.sub()
# #
# # #e = ans2.sub()
# #
# # #print(e)


# ----------------------------------------------------------------
#   String To Dictionary
# try:
#     n = int(input("Enter the number of keys u want to create..."))
#     d = {}
#     for i in range(n):
#         key = input("Enter key : ")
#         value = int(input("Enter Value : "))
#         d[key] = value
#
#     print(d)
#
# except:
#     print("Please enter number..not character")


