l = ["cow", "Goat", "dog", "board"]
d = {}
for i in l:
    i = i[::-1]
    d[i] = len(i)
print(d)


class Animal:

    def typeOfAnimal(self):
        print("pet or wild")


class pet(Animal):

    def color(self):
        print("this is color of animal")

    def typeOfAnimal(self):
        print("pet")


ani = Animal()
ani.typeOfAnimal()

p = pet()
p.typeOfAnimal()
