# from car import info
import car
import methodMe


class addSub:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        c = self.a + self.b
        return c

    def sub(self):
        c = self.a - self.b
        return c


class mulDiv(addSub):
    def __init__(self, a, b):
        super(mulDiv, self).__init__(a, b)

    def mul(self):
        d = self.a * self.b
        return d

    def div(self):
        try:
            d = self.a / self.b
            return d
        except:
            print("This is a Zero division exception")
        else:
            print("this is else statement")
        finally:
            print("Finally the block is executed")
            make = "bmw"
            model = "550i"
            car.info(make, model)

    # def __add__(self):
    #     z = super(mulDiv, self).__add__()
    #     print("class muldiv for add starts from here ...")
    #     return z

    # def sub(self):
    #     #super(mulDiv, self).sub()
    #     super().sub()
    #     print("class muldiv for sub starts from here ...")


class addMul(mulDiv):
    def __init__(self, a, b):
        super(addMul, self).__init__(a, b)


# ans1 = addSub(10, 6)
# print(ans1.__add__())
# print(ans1.sub())

# print('*' * 20)
ans2 = mulDiv(20, 3)
# print(ans2.__add__())

# e = ans2.__add__()
#
# print(e)
# print(ans2.mul())
print(ans2.div())

# print('*' * 20)
z = addMul(100, 99)
print(z.sub())

car = {'make': 'BMW', 'model': '350q', 'year': 2020}
# print(car['make'])
# print(car['model'])
# print(car['year'])
# try:
#     print(car['color'])
# except:
#     print("Caught an exception")
# finally:
#     print("Finally I got an exception")

seq = a[ 0: 100: 2]
print(seq[0: 100: 2])


c = methodMe.Tester.profile()