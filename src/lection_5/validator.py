class ValidateType:
    def __init__(self, type):
        self.name = None  # will be set by metaclass
        self.attr = None  # will be set by metaclass
        self.type = type

    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            return inst.__dict__[self.attr]

    def __set__(self, inst, value):
        if not isinstance(value, self.type):
            raise TypeError('%s must be of type(s) %s (got %r)' %
                            (self.name, self.type, value))
        else:
            print(inst)
            inst.__dict__[self.attr] = value


class Validator(type):
    def __new__(metacls, cls, bases, clsdict):
        # search clsdict looking for ValidateType descriptors
        for name, attr in clsdict.items():
            if isinstance(attr, ValidateType):
                attr.name = name
                attr.attr = '_' + name
        # create final class and return it
        return super().__new__(metacls, cls, bases, clsdict)


class Person(metaclass=Validator):
    weight = ValidateType(int)
    age = ValidateType(int)
    name = ValidateType(str)