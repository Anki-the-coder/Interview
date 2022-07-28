a = 5
b = "10"
'''
mul = a * int(b)
print(mul)

a = "This is a test string"
a[10:3:-2]
Out[17]: 'tas '
a[10:3:-1]
Out[18]: 't a si '
'''

num = [1, 2, 3, 2, 1, 2]
print(num.count(2))
print(len(num))

alpha = ["zero", "one", "two", "five"]
alpha.sort()
print(alpha)
alpha.sort(reverse=1)
print(alpha)

#alpha.reverse()
# print(alpha)
print("-/ "*10)
#print(alpha[-1])

for x in alpha[4:1:-1]:
     print(x)

class person:
     def __init__(self):
          pass

     def data(self, name, age):
          self.name == name
          self.age == age

     def test(self):
          '''

          :return:
          '''