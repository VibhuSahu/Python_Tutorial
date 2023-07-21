x = 4       # global variable
print(f"The value of x is {x} in global")

def hello():
    x = 5       # local variable
    print(f"The value of x is {x} in defination")
    
    
print(f"The value of x is {x} in global")
hello()
print(f"The value of x is {x} in global") 


"""
Output :
The value of x is 4 in global
The value of x is 4 in global
The value of x is 5 in defination
The value of x is 4 in global
"""