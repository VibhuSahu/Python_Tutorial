"""
    # Constructors in Python

Constructors are generally used for instantiating an object. The task of
constructors is to initialize(assign values) to the data members of the
class when an object of the class is created. In Python the _init_()
method is called the constructor and is always called when an object is
created.
"""

class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()        # GeekforGeeks