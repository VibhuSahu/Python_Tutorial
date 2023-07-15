''' Multiline Comment '''

def Defination():
    ''' Docstrings in Python '''
    pass

def sq(n):
    '''
    Takes in a number n, returns the square of n

    Parameters
    ----------
    n

    Returns
    -------
    n^2
    '''
    return n ** 2



print(sq(5))        # Calling function to square the n
print(sq.__doc__)   # To get the Documention


"""
Output :
25

    Takes in a number n, returns the square of n

    Parameters
    ----------
    n

    Returns
    -------
    n^2
    
"""