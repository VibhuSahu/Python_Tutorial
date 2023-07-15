# Factorial
def factorial(n):
    """
    factorial(7) = 7*6*5*4*3*2*1
    factorial(6) = 6*5*4*3*2*1
    factorial(5) = 5*4*3*2*1
    factorial(4) = 4*3*2*1
    factorial(3) = 3*2*1
    factorial(2) = 2*1
    factorial(1) = 1
    factorial(0) = 1

    factorial(n) = n * factorial(n-1)
    """
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)



print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(3))
print(factorial(10))
print(factorial.__doc__)


"""
Output :
1
1
24
6
3628800

    factorial(7) = 7*6*5*4*3*2*1
    factorial(6) = 6*5*4*3*2*1
    factorial(5) = 5*4*3*2*1
    factorial(4) = 4*3*2*1
    factorial(3) = 3*2*1
    factorial(2) = 2*1
    factorial(1) = 1
    factorial(0) = 1

    factorial(n) = n * factorial(n-1)
    

"""