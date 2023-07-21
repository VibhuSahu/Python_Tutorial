def Double(x):
    r = lambda x: x * 2
    return r

cube = lambda x: x ** 3

avg = lambda x, y, z: (x + y + z) / 3


def apple(fx, value):
    return 6 + fx(value)


print(Double(5))
print(cube(5))
print(avg(3, 5, 10))
print(apple(cube, 2))  # Only applicable for lambda function
print(apple(lambda x: x * 3, 4))


"""
Output :
<function Double.<locals>.<lambda> at 0x1028c1e40>
125
6.0
14
18
"""