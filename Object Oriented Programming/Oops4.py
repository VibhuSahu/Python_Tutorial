class Employee:

    increment = 1.5
    no_of_Employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_Employee += 1     # The code work when we access the no_of_Employee with Employee variable.

    def increase(self):
        self.salary = self.salary * Employee.increment


harry = Employee('Harry', 'Jackson', 44000)
rohan = Employee('Rohan', 'Das', 44000)


print(harry.__dict__)       # How to see all instant variable

print(harry.salary)

harry.increase()            # How to use any function

print(harry.salary)

print(harry.__dict__)

print(Employee.no_of_Employee)           # This will print the number of employee we have.
