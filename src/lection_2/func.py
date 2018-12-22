def pow(num, extent):
    return num ** extent

print(pow(3, 3))


def get(a, *args, **kwargs):
    print(a)
    if args != ():
        print(args)
    if kwargs != {}:
        print(kwargs)

print(get(4))
print(get(1, 2, 3))
print(get( 5, 1, 2, 3, 4, s = 5 ))

b = pow()
print()