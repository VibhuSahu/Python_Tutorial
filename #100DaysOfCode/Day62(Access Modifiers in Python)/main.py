class Employee:
    def __init__(self):
        self.__name = "Vibhu Sahu"                 # Private
        
        

a = Employee()

print(a.__dir__())  # it is used get to know accesable attribute
# print(a.__occupation)   # it will throught error it cannot be accessa directly 
print(a._Employee__name)    # The private value can be accessa by this

# In python there is no Proper private public and procted they are just convantion
# And we accessa Private value by name Mangling


"""
Output :
['_Employee__name', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
Vibhu Sahu
"""