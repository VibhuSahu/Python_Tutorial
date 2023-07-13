# While Loops in Python

# Printing 0 to 5 using while loop
def code1():
    i = 0
    while (i < 5):
        print(i)
        i += 1

    print("\n")


#
def code2():
    i = 0
    while (i < 18):
        i = int(input("Enter Number : "))
        print(i)

    print("\n")



def code3():
    i = int(input("Enter Number : "))
    while (i < 18):
        i = int(input("Enter Number : "))
        print(i)

    print("\n")



def code4():
    count = 5
    while (count > 0):
        print(count)
        count -= 1
    else:
        print("I am inside else")

    print("\n")



def code5():
    count = -5
    while (count > 0):
        print(count)
        count -= 1
    else:
        print("I am inside else")

    print("\n")


code1()
code2()
code3()
code4()
code5()