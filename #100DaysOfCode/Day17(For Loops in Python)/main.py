# Printing vibhu sahu with for loop.
def code1():
    name = "Vibhu Sahu"     # String
    for i in name:
        print(i)
        if (i == "b"):
            print("This is something special!")

    print("\n")


# Printing Element of list with for loop.
def code2():
    colors = ["Red", "Green", "Blue", "Yellow"]     # list
    for color in colors:
        print(color)

    print("\n")


# Printing Element and AlphaBets with Nested for loop.
def code3():
    colors = ["Red", "Green", "Blue", "Yellow"]     # list
    for color in colors:
        print(color)
        for i in color:
            print(i)
        print("")

    print("\n")


# Printing 0 to 5 with for loop
def code4():
    for k in range(5):    # Range use to list  0 to 5
        print(k+1)
    print("\n")


# Printing 1 to 25 with gap of 5 using for loop
def code5():
    for u in range(1,25,5):
        print(u)
    print("\n")


# Printing 5 to 0 in decreasing order with for loop
def code6():
    for v in range(5,0,-1):
        print(v)
    print("\n")


# Printing 10 to 0 in decreasing order with gap of 3 using for loop
def code7():
    for j in range(10,0,-3):
        print(j)
    print("\n")



code1()
code2()
code3()
code4()
code5()
code6()
code7()


"""
Output :
V
i
b
This is something special!
h
u
 
S
a
h
u


Red
Green
Blue
Yellow


Red
R
e
d

Green
G
r
e
e
n

Blue
B
l
u
e

Yellow
Y
e
l
l
o
w



1
2
3
4
5


1
6
11
16
21


5
4
3
2
1


10
7
4
1

"""