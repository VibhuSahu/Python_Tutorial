"""
    @classmethod
the @classmehod decorator is used to declare a method in the class
as a class method that can be called using ClassName.MethodName(). The class
method can also be called using an object of the class.

The @classmethod is an alternative of the classmethod() function. It is
recommended to use the @classmethod decorator instead of the function
because it is just a syntactic sugar.


> The first parameter must be cls, which can be used to access class attributes.
> The class method can only access the class attributes but not the instance
  attributes.
> The class method can be called using ClassName.MethodName() and also using
  object.
> It can return an object of the class.


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



harry = Employee("Harry", "Jackson", 44000)
rohan = Employee('Rohan', 'Das',75000)



print(harry.salary)
Employee.change_increment(8)        # This line of code is use to change the value of increment.
harry.increase()                    # This line of code is use to increase the value by given percentage.
print(harry.salary)                 # This line of code finally print the result.