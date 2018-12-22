class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        return self.f


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)

        def wrapper(*args, **kwargs):
            return self.f(cls, *args, **kwargs)

        return wrapper


class InstanceMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        def wrapper(*args, **kwargs):
            return self.f(obj, *args, **kwargs)

        return wrapper


class Property:
    def __init__(self, getter=None, setter=None, deleter=None):
        self.g = getter
        self.s = setter
        self.d = deleter

    def __get__(self, obj, cls=None):
        if self.g is None:
            raise AttributeError

        return self.g(obj)

    def __set__(self, obj, value):
        if self.s is None:
            raise AttributeError

        self.s(obj, value)

    def __delete__(self, obj):
        if self.d is None:
            raise AttributeError

        self.d(obj)


def foo(*args):
    print('foo', args, sep='')


class Bar:
    a = StaticMethod(foo)
    b = ClassMethod(foo)
    c = InstanceMethod(foo)

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value * 2

    def delx(self):
        del self._x

    x = Property(getx, setx, delx)


def main():
    bar = Bar()

    bar.a('static method')
    bar.b('class method')
    bar.c('instance method')

    bar.x = 2

    print(bar.x)


if __name__ == '__main__':
    main()