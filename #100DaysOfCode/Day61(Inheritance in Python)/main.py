import random 


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f'The name of Employee {self.id} is {self.name} ')
        
        
class Programmer(Employee):
    def showLanguage(self):
        print('The default langauge is Python')
        

a = Employee('Vibhu Sahu', random.randint(100, 999))
a.showDetails()

b = Programmer('Das', random.randint(100, 999))
b.showLanguage()


"""
Ouput :
The name of Employee 407 is Vibhu Sahu 
The default langauge is Python
"""