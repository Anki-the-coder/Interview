from selenium.webdriver.common.action_chains import ActionChains

# d = [{"id": "1", "name": "vikash", "age": "26"}, {"id": "2", "name": "jayant"},
#      {"id": "2", "age": "30", "name": "jayant123"}]

# for i in d:
#     try:
#         print(i['name'])
#     except:
#         print("key not present")

# s = "aabbcdeefggg"
# s1 = ""
# for i in s:
#     # if not s.count(i) > 1:
#     if s.count(i) == 1:
#        s1 += i
# print(s1)
# # s2 = [i for i in s if s.count(i) == 1]
# # print(s2)
# # s4 = ''.join(s2)
# # print(s4)
#
# print(s1[0])

s = "This is a is is forest. Forest Green is so forest Green. Grass forest is also a Green Green Green forest."
count = 0
for i in s:
    if i in "!?',;.":
        s = s.replace(i, "")
l = s.split()
d = {}
for i in l:
    count += 1
    i = i.lower()
    if i in d:
        d[i.lower()] += 1
    else:
        d[i.lower()] = 1
print(d)
d2 = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(d2)
print(d2[0])
# fo = max(d.values())
# key_l = list(d.keys())
# print(key_l)
# val = list(d.values())
# print(val)
# pos = val.index(fo)
# print(key_l[pos])
