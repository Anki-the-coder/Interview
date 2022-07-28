
s = "Ankush Channe Tester"
s = s.split()
s1 = ' '.join(s[::-1])
print(s1)

str1 = "12abc20yz68"
temp = "0"
total = 0
for i in str1:
    if i.isdigit():
        temp += i
    else:
        total += int(temp)
        temp = "0"
tot1 = total + int(temp)


# print(total)


class test_ME:

    def __init__(self, paint):
        self.paint = paint

    def test_iMTested(self):
        print(f"Hi, I am Genius with {self.paint} shirt")


class test_other(test_ME):

    def test_otherTested(self):
        print("Hi, Others are dumb")


obj1 = test_ME("red")
# obj1.test_iMTested()

obj2 = test_other("Blue")
# obj2.test_otherTested()
# obj2.test_iMTested()


list1 = [5, 15, 51, 35, 40, 10]
print(list1[-2])
print(list1[-1])
print(list1[-2] >= list1[-1])


# yyyy-mm-dd format to dd-mm-yyyy format
initial = "yyyy-mm-dd"
for i in initial:
    if i in "-":
        initial = initial.replace(i, " ")

initial = initial.split()
newDate = '-'.join(initial[::-1])
print(newDate)


s = "Www.HackerRank.com"
# → wWW.hACKERrANK.COM"
s1 = ""
for i in s:
    if i == i.lower():
        s1 += i.capitalize()
    else:
        s1 += i.lower()
print(s1)

names = ["mumbai", "pune", "banglore", "daund", "nasik", "pates", "gpl"]
d1 = {}
vowels = "aeiou"
for i in names:
    d1[i] = 0
    for j in i:
        if j in vowels:
            d1[i] += 1
print(d1)
