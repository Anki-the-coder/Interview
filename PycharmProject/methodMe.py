'''
states: ["nyc", "la"]

def income1(state, gross):
    if state == 'nyc':
        fed_tax = gross / 10
        state_tax = gross * 0.09
        print("tax for nyc is ")
    elif state == 'la':
        fed_tax = gross / 10
        state_tax = gross * 0.07
        print("tax for la is ")
    else:
        print("Entered state is not correct")
        return None

    net_income = gross - (fed_tax + state_tax)
    return net_income

income1('la', 120)
#print(income2)


name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"


#greeting(3842)
print(greeting(3482))


def stating(dry_State, incom)

8888888888888

class Car(object):

    def __init__(self, make, year, model="550i"):

        self.make = make
        self.model = model
        self.year = year

c1 = Car('bmw', 2019)
print(c1.make)
print(c1.model)
print(c1.year)

c2 = Car('benz', 2018)
print(c2.make)
print(c2.model)
print(c2.year)
888888888888888
'''


class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = Car('bmw', '550i')
# print(c1.make)
# c1.info()

c2 = Car('benz', 'E350')


# print(c2.make)
# c2.info()

# print(Car.wheels)


class Tester:
    ISTQB = True

    def __init__(self, manual, automation):
        self.manual = manual
        self.automation = automation

    def profile(self):
        #print("My manual exp is " + self.manual)
        #print("My automation exp is " + self.automation)
        print("My automation exp is test")

    def init1(self, python, java):
        print("My python exp is", python)
        print("My java exp is", java)


class Certified(Tester):

    def __init__(self, white, black):
        super(Certified, self).__init__(self, manual, automation)
        super().profile()

    def profile(self):
        print("My manual exp is " + self.manual)
        print("My automation exp is " + self.automation)

    def black(self, white, black):
        print("My white exp is", white)
        print("My black exp is", black)

"""
test1 = Tester('4', '2')
#test1.profile()

test3 = Tester('4', '2')
test3.init1([5,6], 6)
#test3.init1('5', '7')

#test2 = Tester('8', '10')
#test2.profile()

#print(type(Tester.ISTQB))
"""

test1 = Tester('14', '12')
test1.profile()

test4 = Certified(11, 17)
test4.black(10, 16)
#print(test4)

test4.profile()