# Question. Write a program to print the following pattern :

def zPattern(num):
    """
    Parameters
    ----------
    num

    Returns
    -------
    It return's the * in z pattern
    """
    print(" * " * num)
    for x in range(num-2, 0, -1):
        print("   " * x, "*")
    print(" * " * num)


zPattern(int(input("    Enter any number : ")))

"""
Output :
    Enter any number : 10       # User input
 *  *  *  *  *  *  *  *  *  * 
                         *
                      *
                   *
                *
             *
          *
       *
    *
 *  *  *  *  *  *  *  *  *  * 
"""