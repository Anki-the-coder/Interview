# mylist = [10, 20, 30, 20, 30, 40, 40]
# # mylist1 = []
# #
# #
# # # def func(mylist, k):
# # #     for i in range(len(mylist)):
# # #         try:
# # #             a = k - mylist[i]
# # #             if a in mylist:
# # #                 if a not in mylist1:
# # #                     print(mylist[i], a)
# # #                     mylist1.append(a)
# # #                     mylist1.append(mylist[i])
# # #         except:
# #             break
#
#
# func(mylist, 50)

# mylist = [10, 20, 30, 40]
# mylist1 = []
#
#
# def func(mylist, k):
#     for i in range(len(mylist) - 1):
#         a = k - mylist[i]
#         if a in mylist:
#             print(mylist[i], a)


# func(mylist, 50)


mylist = [10, 20, 30, 20, 30, 40, 40]
mylist1 = []


def func(mylist, k):
    for i in range(len(mylist)):
        a = k - mylist[i]
        if a in mylist and a not in mylist1:
            print(mylist[i], a)
            mylist1.append(a)
            mylist1.append(mylist[i])


func(mylist, 50)

#
# import requests
# stud = []
# count = 1
# d= {}
#
# class clg:
#
#     def __init__(self, name, last, dept):
#         self.name = name
#         self.last = last
#         self.dept = dept
#
#
#     def admission(self):
#         # count += 1
#         stud1 = []
#         # stud1.append(count)
#         stud1.append(self.name)
#         stud1.append(self.last)
#         stud1.append(self.dept)
#         stud.extend(stud1)
#
#
#     def DeleteInfo(self, name, last, dept):
#         stud.pop()
#
# a = clg("Ramesh", "josh", "Civil")
# a.admission()
# a = clg("Ramesh1", "josh1", "Civil1")
# a.admission()
# print(stud)
#
# print(stud[::3])
#
#
#
#
# def test_studentAmission:
#     assert stud[0] == "Ramesh"
#
# def test_updateData
#     assert stud[0] == "Ramesh"
#
# def test_invalidStudent:
#     assert stud[0] == "Suresh"
#
# def test_Deletestudy:
#     assert stud[0] == "Ramesh"
