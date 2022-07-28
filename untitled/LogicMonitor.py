# Problem 1 - Find count on element in the nested list

list1 = ["abc", "pqr", ["efg", "abc", ["pqr", "lmn"], "pqr"], "efg"]
list2 = []
d = {}


def createFlatList(list1):
    for i in list1:
        if type(i) == list:
            createFlatList(i)
        else:
            list2.append(i)


createFlatList(list1)
print(list2)
for j in list2:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

print(d)

# Problem 2 - find if 2 strings a anagram or not

s1 = input("Please enter the 1st string: ")  # "forty five"
s2 = input("Please enter the 2nd string: ")  # "over fifty"

print(sorted(s1))
print(sorted(s2))

if sorted(s1) == sorted(s2):
    print("String is Anagram")
else:
    print("String is not Anagram")
