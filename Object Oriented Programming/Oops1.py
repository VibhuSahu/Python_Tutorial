"""
    # Encapsulation in Python

Encapsulation is a mechanism of wrapping the data(Variables) and code
acting on the data(methods) together as a single unit. In encapsulation, the
variables of a class will be hidden from other classes, and can be accessed only
through the methods of their current class.

    # Polymorphism in Python
Polymorphism in python degines methods in the
child class that have the same name as the
methods in the parent class. In inheritance, the
child class inherits the methods from the parent class.
Also, it is possible to modify a method in a child class
that it has inherited from the parent class.

"""

class Employee:
    pass


Harry = Employee()
Rohan = Employee()


# Object first Harry
Harry.fname = 'Harry'
Harry.lname = 'Jackson'
Harry.salary = '44000'


# Object second Rohan
Rohan.fname = 'Rohan'
Rohan.lname = 'Das'
Rohan.salary = '44000'


print(Harry.fname)      # Harry


print(Harry)            # <__main__.Employee object at 0x1027e1910>


print(Harry, Rohan)     #<__main__.Employee object at 0x102825910> <__main__.Employee object at 0x102825950>