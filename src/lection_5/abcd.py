class A():
    x = 1
    def __init__(self):
        print(f"{self.__class__}")

class B(A):
    x = 2
    def __init__(self):
        super().__init__()
        print(f"{self.__class__}")

class C(A):
    x = 3
    def __init__(self):
        super().__init__()
        print(f"{self.__class__}")


class D(C, B):
    def __init__(self):
        super().__init__()
        print(f"{self.__class__}")

a = A()
print(a.x)
b = B()
print(b.x)
c = C()
print(c.x)
d = D()
print(d.x)
print(D.mro())
