def gen():
    print(1)
    yield
    print(2)
    yield


g = gen()
print(list(g))
print(g)
print(g.__next__())
g.send(12)
print(g.__next__())
print(g.__next__())