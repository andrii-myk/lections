class A():
    x = 1
    def __init__(self):
        print(f"{self.__class__}")

    #def __getattr__(self, item):
        #if item == self.x:
        #    return 12
        #else:
        #    return None

    def __getattribute__(self, item):
        if item == 'abc':
            return 'asdas'
        else:
            print(item)
            return None


a = A()
#print(a.__getattr__(a.x))
a.abc = "abc"
print(a.__dict__)