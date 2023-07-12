"""
# Question. What is the output of the following python program? First try and predict the output
            without the computer. Check your answer by typing answer by typing it in and running it.
"""
i = 0
while i < 6:
    j = 0
    while j < i:
        print("*",end=" ")
        j = j + 1
    i = i + 1
    print()

"""
Output :
* 
* * 
* * * 
* * * * 
* * * * * 
"""