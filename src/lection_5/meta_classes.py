def foo():
    def bar():
        return "123"
    return bar()

print(foo())


class A():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, number):
        self.number = number


class XInt(int):
    def __new__(cls, z):
        return super().__new__(cls, z*2)



x = XInt(2)

print(type(XInt))
print(type(XInt(2)))
print(type(type(XInt)))