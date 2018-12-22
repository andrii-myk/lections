x = 'abc'

def a():
    x = 2

def b():
    global x
    x = 2
print(x)
a()
print(x)
b()
print(x)