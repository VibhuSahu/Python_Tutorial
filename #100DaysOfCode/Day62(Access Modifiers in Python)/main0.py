class Employee:
    def __init__(self, name, occupation):
        self._name = name                   # Protected
        self.__occupation = occupation      # Private
        

a = Employee('Vibhu Sahu', 'Web Devlopment')


print(a._name)

"""
Output :
Vibhu Sahu
"""