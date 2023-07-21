def greet(fx):
    def mfx(*args, **kwargs):       # *args is for list and **kwargs is for dictionary
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx


def hello():
    print('Hello, World!')


def adding(a, b):
    print(a + b)
    


greet(adding)(1, 2)

"""
Output :
Good Morning
3
Thanks for using this function
"""