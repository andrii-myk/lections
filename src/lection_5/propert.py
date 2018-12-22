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


