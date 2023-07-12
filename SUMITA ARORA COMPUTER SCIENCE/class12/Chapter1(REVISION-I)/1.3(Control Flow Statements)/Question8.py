# Question. Write programs that generate each of the patterns given below.

def triangleUpSideDown(num):
    for x in range(num, 0, -1):
        print(" * " * x)
    print("\n\n")

def twoSquare(num):
    for a in range(num, 0, -1):
        print("   " * num, " * " * num)
    for b in range(num, 0, -1):
        print(" * " * num)
    print("\n\n")

def holeInSquare(num):
    print(" * " * num)

    div = num//2
    if (div % 2 == 0):
        for y in range(div, 0, -1):
            print(" * " * y, "  " * (div - y), end=" ")
            print('   ' * (div - y) + ' * ' * y)
        for z in range(1, div + 1):
            print(" * " * z, "   " * (div - z), end=" ")
            print( '   ' * (div - z) + ' * ' * z)
        print(" * " * num)

    else:
        for y in range(div, 0, -1):
            print(" * " * y, "   " * (div - y), end="  ")
            print('   ' * (div - y) + ' * ' * y)
        for z in range(1, div + 1):
            print(" * " * z, "   " * (div - z), end="  ")
            print('   ' * (div - z) + ' * ' * z)
        print(" * " * num)





triangleUpSideDown(10)
twoSquare(10)
holeInSquare(10)