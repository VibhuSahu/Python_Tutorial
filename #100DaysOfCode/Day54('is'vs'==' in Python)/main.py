def code1():
    a = 4
    b = '4'
    
    print(a is b)    # exact location of object in memory
    print(a == b)    # value 
    
    """
    Output:
    False
    False
    """
    

def code2():
    a = [1, 2, 43]
    b = [1, 2, 43]
    
    print(a is b) # exact location of object in memory
    print(a == b) # value
    
    """
    Output :
    False
    True
    """


def code3():
    a = 3
    b = 3
    
    print(a is b) # exact location of object in memory
    print(a == b) # value
    
    """
    Output :
    True
    True
    """


def code4():
    a = (1, 2)
    b = (1, 2)
    
    print(a is b) # exact location of object in memory
    print(a == b) # value
    
    """
    Output :
    True
    True
    """


def code5():
    a = None
    b = None
    
    print(a is b) # exact location of object in memory
    print(a is None) # exact location of object in memory
    print(a == b) # value
    
    """
    Output :
    True
    True
    True
    """





# code1()
# code2()
# code3()
# code4()
# code5()