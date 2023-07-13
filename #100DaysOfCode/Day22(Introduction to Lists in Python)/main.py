
def isThere(ls, value):
    if value in ls:
        print("Yes")
    else:
        print("No")


def onIt(val1, val2):
    if val1 in val2:
        print("Yes")
    else:
        print("No")


def lsAlphabet():
    return [chr(i) for i in range(97, 123)]         # one line for loop inside a list


def oneLineList():
    ls1 = [i for i in range(10)]
    ls2 = [i*i for i in range(10)]

    return [ls1, ls2]


def oneLineListWithCondition():
    ls = [i*i for i in range(25) if i%2==0]
    return ls




ls = [3, 5, 6, "Harry", True]

print(ls)           # Print list with Print statments
print(*ls)          # Print list Element without bracket

print(type(ls))     # data type of variable     # list is class it self

print(ls[0])        # Printing element with index
print(ls[1])
print(ls[2])
print(ls[3])
print(ls[4])

print(ls[-1])       # Printing element from backward with index
print(ls[-2])
print(ls[-3])
print(ls[-4])
print(ls[-5])


isThere(ls, "Harry")

onIt('ry', 'Harry')


print(ls)
print(ls[1:-1])
print(*ls[1:-1])


print(lsAlphabet())
print(*(lsAlphabet()))


print(lsAlphabet()[1:8])
print(*(lsAlphabet()[1:8]))
print(lsAlphabet()[1:19:3])
print(*(lsAlphabet()[1:19:3]))


print(oneLineList()[0])
print(*oneLineList()[0])
print(oneLineList()[1])
print(*oneLineList()[1])


print(oneLineListWithCondition())
print(*oneLineListWithCondition())


"""
Output :
[3, 5, 6, 'Harry', True]
3 5 6 Harry True
<class 'list'>
3
5
6
Harry
True
True
Harry
6
5
3
Yes
Yes
[3, 5, 6, 'Harry', True]
[5, 6, 'Harry']
5 6 Harry
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a b c d e f g h i j k l m n o p q r s t u v w x y z
['b', 'c', 'd', 'e', 'f', 'g', 'h']
b c d e f g h
['b', 'e', 'h', 'k', 'n', 'q']
b e h k n q
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0 1 2 3 4 5 6 7 8 9
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
0 1 4 9 16 25 36 49 64 81
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576]
0 4 16 36 64 100 144 196 256 324 400 484 576

"""