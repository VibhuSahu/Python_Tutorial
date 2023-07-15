def code1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index : "))
        print(l[i])
    except:
        print("Sorry! Some error occurred")
    finally:
        print("I am always executed")

    print("\n")


def code2():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index : "))
        return l[i]
    except:
        print("Sorry! Some error occurred")
        return 0
    finally:
        print("I am always executed")

    print("\n")


def code3():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Sorry! Some error occurred")
        return 0
    finally:
        print("I am always executed")

    print("\n")


def code4():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Sorry! Some error occurred")
        return 0
    finally:
        return "I am always executed"

    print("\n")



code1()
code1()

print(code2())

print(code3())

print(code4())


"""
Output :
Enter the index : 1     # input
5
I am always executed


Enter the index : df    # input
Sorry! Some error occurred
I am always executed


Enter the index : 2     # input
I am always executed
6
Enter the index : df    # input
Sorry! Some error occurred
I am always executed
0
Enter the index : 2     # input
6
I am always executed

"""