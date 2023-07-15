# Fibonacci sequence
def Fibonacci(n):
    '''
    f(n) = f(n-1) + f(n-2)
    Parameters
    ----------
    n

    Returns
    -------
    f(0) = 0
    f(1) = 1
    f(2) = f(1) + f(0)
    f(n) = f(n-1) + f(n-2)
    '''
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(0))
print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))
print(Fibonacci(8))
print(Fibonacci(9))
print(Fibonacci(10))


"""
Output :
0
1
1
2
3
5
8
13
21
34
55
"""