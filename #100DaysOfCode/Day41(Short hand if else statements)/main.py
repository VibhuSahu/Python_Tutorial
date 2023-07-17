def code1(a, b):
    return "A" if a>b else "=" if a==b else "B"


def code2(a, b):
    c = 9 if a>b else 0
    return c



print(code1(33, 3303))
print(code1(33, 33))
print(code1(3303, 33))


print(code2(3303, 33))
print(code2(33, 33))
print(code2(33, 3303))


"""
Output :
B
=
A
9
0
0
"""