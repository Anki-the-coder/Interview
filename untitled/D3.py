class A:

    def __init__(self, y, z):
        self.y = y
        self.z = z

    def test(self):
        return self.z + self.y

    def test1(self):
        return print(self.z + self.y)


a = A(4, 5)


class B(A):

    def __init__(self, x, y, z):
        super().__init__(y, z)
        self.x = x
        self.y = y
        self.z = z

    def test(self):
        print("From class B")


objB = B(3, 4, 5)
# objB.test("self")
objB.test1()

