class Employee:

    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2.5

    def increase(self):
        self.salary = self.salary * Employee.increment



harry = Employee('Harry', 'Jackson', 44000)
rohan = Employee('Rohan', 'Das', 44000)


print(harry.__dict__)       # How to see all instant variable

print(harry.salary)

harry.increase()            # How to use any function

print(harry.salary)

print(harry.__dict__)