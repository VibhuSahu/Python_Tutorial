"""
# Question. Consider the following code:

    if y has the value 2 after executing the above program fragment, then what do you know
    about the initial value of x?
"""
x = 7       # it give 2 be the value of y where x is 7
if x > 3:
    if x <= 5:
        y = 1
    elif x != 6:
        y = 2
    else:
        y = 3
else:
    y = 4

print(y)
"""
Output :
2
"""