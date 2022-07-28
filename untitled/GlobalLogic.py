# Problem 1 - Print any random no. || Print any random no from a range
import random

ranNo = random.random()
ran = random.randint(10, 220)
print(ranNo)
print(ran)

# Problem 2 - Remove "u" from string "Ankush"
s = "ankush"
s5 = ""
for i in s:
    if i != "u":
        s5 += i
print(s5)

# Problem 3 - print the string "ankush" in the format - "knahsu"
s1 = s[::-1]
s2 = s[2::-1]
s3 = s[6:2:-1]
s4 = s2 + s3
print(s2)
print(s3)
print(s4)


# Problem 4 - Write test on application to upload pdf file
# Problem 5 - Write negative test cases on sending text messages from mobile
# Problem 6 - How will you cut the cake in 8 equal parts in 3 cuts

# how to copy an object
import copy

#for shallow copy use copy
# for deep copy, use copy.deepcopy
