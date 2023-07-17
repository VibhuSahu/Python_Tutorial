"""
Linter - Programs that advise about code quality by displaying warnings and errors.
"""

def code1(marks):
    for mark in marks:
        print(mark)
        if (marks[3] == mark):
            print("Vibhu, awesome!")
    print("\n")
            
            

def code2(marks):
    index = 0
    for mark in marks:
        print(mark)
        if (index == 3):
            print("Vibhu, awesome!")
        
        index += 1
    print("\n")
    
    

def code3(marks):
    for index, mark in enumerate(marks):
        print(index, mark)
        if (index == 3):
            print("Vibhu, awesome!")
            
    print("\n")
            
            
def code4(marks):
    for index, mark in enumerate(marks, start=1):
        print(index, mark)
        if (index == 3):
            print("Vibhu, awesome!")
            
    print("\n")
            
      
      
            
      
ls = [12, 56, 32, 98, 12, 45, 1, 4]      

code1(ls)
code2(ls)
code3(ls)
code4(ls)




""" 
Output :
12
56
32
98
Vibhu, awesome!
12
45
1
4


12
56
32
98
Vibhu, awesome!
12
45
1
4


0 12
1 56
2 32
3 98
Vibhu, awesome!
4 12
5 45
6 1
7 4


1 12
2 56
3 32
Vibhu, awesome!
4 98
5 12
6 45
7 1
8 4

"""