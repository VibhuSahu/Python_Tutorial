x = 4
y = 8

def hello():
    global x    # diclaring x as global
    x = 5
    print(f"The local s is {x}")
    
    
print(f"The global x is {x}")
hello()
print(f"The global x is {x}")


"""
Output :
The global x is 4
The local s is 5
The global x is 5
"""
# using global key is not great practice