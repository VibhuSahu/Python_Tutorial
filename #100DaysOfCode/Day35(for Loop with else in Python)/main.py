def forElsefunction(n):
    for i in range(n):
        print(i)
        if i == 4:
            break
    else:
        print("Sorry no i")

    print("\n")


def whileElsefunction(n):
    i = 0
    while i < n:
        print(i)
        i += 1
        if i == 8:
            break
    else:
        print("Sorry no i")

    print("\n")


def forAnotherOne(n):
    for x in range(n):
        print("iteration no {} in for loop".format(x+1))
    else:
        print("else block in loop")
    print("Out of loop")
    print('\n')



val = int(input("Enter a number : "))

forElsefunction(val)
whileElsefunction(val)
forAnotherOne(val)

"""
Output :
Enter a number : 5      # user Input
0
1
2
3
4


0
1
2
3
4
Sorry no i


iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop


"""