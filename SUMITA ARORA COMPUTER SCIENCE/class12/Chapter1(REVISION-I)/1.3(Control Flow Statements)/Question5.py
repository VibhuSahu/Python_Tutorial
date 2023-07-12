"""
# Question. Consider the following two fragments:

    Are the two fragments logically equivalent? Why or why not?
"""
#   (a)


if x == 5:
    x = x + 1
else:
    x = 8
print(x)

#   (b)

if x == 5:
    x = x + 1
if x != 5:
    x = 8
print(x)