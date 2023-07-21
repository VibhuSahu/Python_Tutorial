def code1():
    def cube(x):
        return x * x * x

    l = [1, 2, 4, 6, 4, 3]
    newm = map(cube, l)
    newl = list(map(cube, l))
    
    print(newm)
    print(newl)
    print('\n')
    
    
def code2():
    def cube(x):
        return x * x * x
    
    def filter_function(a):
        return a > 3

    
    l = [1, 2, 4, 6, 4, 3]
    newm = map(cube, l)
    newl = list(map(cube, l))
    
    print(newm)
    print(newl)
    
    newnewf = filter(filter_function, l)
    newnewl = list(filter(filter_function, l))
    print(newnewf)
    print(newnewl)
    print('\n')
    

def code3():
    l = [1, 2, 4, 6, 4, 3]
    newl = list(map(lambda x: x * x * x, l))
    print(newl)    
    print('\n')



def code4():
    """
    l = [1, 2, 3, 4, 5]
    1 + 2 = 3   --> [3, 3, 4, 5]
    3 + 3 = 6   --> [6, 4, 5]
    6 + 4 = 10  --> [10, 5]
    10 + 5 = 15 --> [15]
    """
    from functools import reduce
    
    number = [1, 2, 3, 4, 5]
    
    sum = reduce(lambda x, y: x + y, number)
    print(sum)
    print('\n')
    
    
    
def code5():
    """
    l = [1, 2, 3, 4, 5]
    1 * 2 = 2    ---> [2, 3, 4, 5]
    2 * 3 = 6    ---> [6, 4, 5]
    6 * 4 = 24   ---> [24, 5]
    24 * 5 = 120 ---> [120]
    """
    from functools import reduce
    
    def multiple(a, b):
        return a * b
    
    number = [1, 2, 3, 4, 5]
    
    mul = reduce(multiple, number)
    print(mul)

    
    
code1()
code2()
code3()
code4()
code5()

"""
Output :
<map object at 0x10228bfd0>
[1, 8, 64, 216, 64, 27]


<map object at 0x10228bca0>
[1, 8, 64, 216, 64, 27]
<filter object at 0x10228bbb0>
[4, 6, 4]


[1, 8, 64, 216, 64, 27]


15

120
"""