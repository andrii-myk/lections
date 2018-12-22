int_x = 5
float_y= 0.2
str ="Hi!"
tup = (1, 2, 'Light')

map = {"python": "Van Roassum", "c": "Ritchi"}
list = [0.2, 5.6, 3.2]
print(map)
s = set([3, 5, 8, 13, 21])
print(s)
print(1/3)
v = 'abx'
u = f'abc {int_x}'
print(u)

try:
    print(1/0)
except(ZeroDivisionError):
    print("You can not divide by zero")
finally:
    print("Some text")