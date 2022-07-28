class Fruit:
    def __init__(self):
        pass

    def nutrition(self):
        print("Fruits have good nutrition")

    def fruit_shape(self):
        print("Shape of Apple is like Apple")


class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)

    def nutrition(self):
        super().nutrition()
        print("Fruits have good nutrition from Apple")

    def color(self):
        Apple.nutrition(self)
        print("Apple is Red")


a = Fruit()
a.nutrition()
a.fruit_shape()

print('*'*20)

b = Apple()
b.nutrition()
b.fruit_shape()
b.color()