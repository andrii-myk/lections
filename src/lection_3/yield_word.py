def b():
	print(1)
	yield 1.5
	print(2)
	yield 2.5

x = b()
print(next(x))
print(next(x))

print("Using for")
x = b()
for i in x:
    print(i)

