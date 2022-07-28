s = "Programming"
l = s.split()
d = {}
for i in s:
    l.append(i)
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# print(d)
print(max(d.items()))

