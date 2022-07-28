a = [1, 3, 4, 7, 3, 14, 25]
k = 2
# a = [14, 25, 1, 3, 4, 7]
b = []
for i in range(-k, len(a) - k):
    b.append(a[i])
print(b)
