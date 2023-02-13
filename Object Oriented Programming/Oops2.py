"""
    # Template

You all of any class as a template.
"""

class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

harry = Employee('Harry', 'Jackson', 44000)
rohan = Employee('Rohan', 'Das', 44000)

print(harry,rohan)                  #  <__main__.Employee object at 0x104b55b10> <__main__.Employee object at 0x104b55c50>


print(harry.fname , rohan.lname)    # Harry Das