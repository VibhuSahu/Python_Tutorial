import random as fuck

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


for _ in range(5):
    value = fuck.randint(10, 100)
    print(f"    the Number is : {value}.")
    holeInSquare(value)
    print("\n\n")