# l1 = []
# size = int(input("Enter the size of array: "))
# for i in range(0, size):
#     value = int(input("Enter the elements in the list: "))
#     l1.append(value)
# a = 0
# print(l1)
# sum1 = int(input("Enter the sum: "))
# for i in l1:
#     for j in range(a + 1, len(l1)):
#         if i + l1[j] == sum1:
#             print("Values are: ", i, l1[j])
#     a += 1


# s = "This is a forest. Forest is so Green. Grass is also a Green forest."
# count = 0
# for i in s:
#     count += 1
#     if i in "!?',;.":
#         s = s.replace(i, "")
# l = s.split()
# d = {}
# for i in l:
#     i = i.lower()
#     if i in d:
#         d[i.lower()] += 1
#     else:
#         d[i.lower()] = 1
# print(d)
#
# avg = count / len(l)
# # print(round(avg))
#
# # y = []
# # s = s.replace(" ", "")
# # for i in s:
# #     if i in ".":
# #         s = s.replace(i, "")
# #     if not i.lower() in y:
# #         y.append(i.lower())
# #         # print(i, "and", s.index(i))
#
# b = "This is a forest. Forest is so Green. Grass is also a Green forest."
# c = "This is a forest. My Car is Blue. Africa has Green forest."
# print(b)
# for i in range(len(b)):
#     t = (b[:i] + b[i+1:])
#     print(t[::-1])


# b = b.split()
# c = c.split()
# match = []
# unMatch = []
# # for i in b:
# #     for j in c:
# #         if i.lower() == j.lower():
# #             if i.lower() not in match:
# #                 match.append(i.lower())
# #         else:
# #             if i.lower() not in unMatch:
# #                 unMatch.append(j.lower())
# # print(match)
# # print(unMatch)
# for i in b:
#     if i in c:
#         if not i in match:
#             match.append(i)
#     else:
#         if not i in unMatch:
#             unMatch.append(i)
#
# for i in c:
#     if i in b:
#         if not i in match:
#             match.append(i)
#     else:
#         if not i in unMatch:
#             unMatch.append(i)
# # print(match)
# # print(unMatch)
#
# st = ' '.join(unMatch)
# tu = set(unMatch)
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
# print([[x, weekdays.count(x)] for x in weekdays])
names = ['Chris', 'Jack', 'John', 'Daman']
# print(names[-2])

#
subjects = ('Python', 'Interview', 'Questions')
for subject in enumerate(subjects):
    # print(subject)

#
# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
#
# print(names1[::2])
#
# names2[0] = 'Alice'
# names3[1] = 'Bob'
#
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
# if ls[1] == 'Bob':
#     sum += 10
#
# # print(sum)
#

# from distlib.compat import raw_input
#
# s1 = raw_input("Enter first string:")
# s2 = raw_input("Enter second string:")
# a = list(set(s1) & set(s2))
# print("The common letters are:")
# print(a)
# for i in a:
#     print(i)
#

# sent = "This is a forest"
# words = sent.split()
# n1 = []
#
# for word in words:
#     n1.append(word[::-1])
#
# res_str = " ".join(n1)
# print(res_str)

