#
# a = [1, 2, 5, 3, 4, 3]
# b = 3
# n = 0
# n1 = int(n+3)
# l1 = []
# while n1 <= len(a):
#     for i in range(int(a[n]), int(a[n1])):
#         if i not in l1:
#             l1.append(i)
#         print(l1)
#     l1 = []
#     n += 1
#     n1 += 1

#
# # s = "This is a forest. Forest is so Green. Grass is also a Green forest."
# file = open("C:\\Users\\channank\\Desktop\\dtcs.txt")
# s = file.read()
# file.close()
# count = 0
# for i in s:
#     if i in "!?',;.":
#         s = s.replace(i, "")
# l = s.split()
# d = {}
# for i in l:
#     count += 1
#     i = i.lower()
#     if i in d:
#         d[i.lower()] += 1
#     else:
#         d[i.lower()] = 1
# print("Total word count is: " + str(count))
# n = 3
# sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
# for j in range(0, n):
#     print(sort_orders[j])


imported_list = [2, 44, 3, 3, 5, 3, 3, 4]
l1 = [1, 3, 4, 7, 14, 25]
print(l1[0:3])
print(l1[1:4])
print(l1[2:5])
print(l1[3:6])

# j = 4
# i = 0
# for list_item in range(len(imported_list) - 3):
#     for sub_list_item in range(i, j):
#         final_list = imported_list[i:j]
#
#         print(final_list)
#         i += 1
#         j += 1
#
#         unique_list_from_final_list = []
#         for r in final_list:
#             if final_list.count(r) == 1:
#                 unique_list_from_final_list.append(r)
#         print(unique_list_from_final_list)
#         break



s = "aabbcde"
token= "oalwiz3ut65b"
s1 = ""
# s2 = ""
for i in s:
    if i not in s1:
        s1 += str(s.count(i))
        s1 += i
# i
# for i in s1:
#     if i not in token:
#         s2 += str(i)
s2 = [i for i in s1 if i not in token]
s3 = ''.join(s2)
print(s1)
print(s3)

for i in s:
    if s.count(i) > 1:
        pass
    else:
        print(i)
        break


name = "ankush"
# name = name[::-1]
# print(name)

fn = "Ankush Channe Tester"
# fn = fn.split()
# fn1 = ' '.join(fn[::-1])
# print(fn1)


name1 = ""
for i in name:
    name1 = i + name1
print(name1)

fn1 = ""
for i in fn:
    fn1 = i + fn1
print(fn1)

