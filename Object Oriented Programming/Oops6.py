"""
    @staticmethod
There can be some functionality that relates to the class, but does not require any
instance(S) to do some work, static methods can be used in such cases. A static
method is a method which is bound to the class and not the object of the class. it can't
access or modify class state. it is present in a class because it makes sense for the
method to be present in class. A static method does not receive an implicit first
argument.
"""


class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod                    # This classmethod is use to specify any value.
    def change_increment(cls,amount = 1.5):
        cls.increment = amount

    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True



harry = Employee("Harry", "Jackson", 44000)
rohan = Employee('Rohan', 'Das',75000)



print(harry.salary)
Employee.change_increment(8)        # This line of code is use to change the value of increment.
harry.increase()                    # This line of code is use to increase the value by given percentage.
print(harry.salary)                 # This line of code finally print the result.

print(Employee.isopen('monday'))    # This will verify whether the isopen is True or false.
