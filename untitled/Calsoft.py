x = (1, 2, 3, 4, 9, 9, 5, 5)
l = []
for i in x:
    l.append(i)
l.sort()
m = m2 = 0
for i in l:
    if i > m:
        m2 = m
        m = i
print(m2)
