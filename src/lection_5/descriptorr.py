class X():
    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return "const"

class Z():
    x = X()
    def __init__(self):
        print(x)
        print(X)

x = X()
z = Z()


def foo(*args):
    print(args)

z.foo = foo()
print(z.foo)