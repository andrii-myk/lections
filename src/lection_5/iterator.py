class X():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.b:
            self.i += 1
            return self.i
        else:
            raise StopIteration

x = X(1, 10)
while x:
    print(x.__next__())
print(x.__next__())