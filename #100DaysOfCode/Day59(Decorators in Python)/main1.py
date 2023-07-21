def greet(fx):
    def mfx(*args, **kwargs):       # *args is for list and **kwargs is for dictionary
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx


def hello():
    print('Hello, World!')

@greet
def adding(a, b):
    print(a + b)
    


adding(1, 2)

"""
Output :
Good Morning
3
Thanks for using this function
"""