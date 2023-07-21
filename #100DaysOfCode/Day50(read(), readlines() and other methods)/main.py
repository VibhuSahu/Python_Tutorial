def readlineFile():
    """
    Reading file element line by line and it's type.
    """
    f = open("#100DaysOfCode/Day50(read(), readlines() and other methods)/message1.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
  
  
def readlineFile2():
    """
    Reading file element line by line and it's type.
    """
    f = open("#100DaysOfCode/Day50(read(), readlines() and other methods)/message1.txt", "r")
    while True:
        line = f.readline()
        print(line)                         
        if not line:
            print(line, type(line))
            break      
        

def readingArrFile():
    """
    Reading an array from text files using `readlines()` method. 
    """
    with open('#100DaysOfCode/Day50(read(), readlines() and other methods)/message2.txt', "r") as f:
        i = 0
        while True:
            i = i + 1
            line = f.readline()
            if not line:
                break 
            
            m1 = line.split(',')[0]
            m2 = line.split(',')[1]
            m3 = line.split(',')[2]

            print(f'Marks of student {i} in maths is: {m1}')
            print(f'Marks of student {i} in maths is: {m2}')
            print(f'Marks of student {i} in maths is: {m3}')
        


def readingArrFile2():
    """
    Reading an array from text files using `readlines()` method, converting each element into integer type before
    """
    with open('#100DaysOfCode/Day50(read(), readlines() and other methods)/message2.txt', "r+") as f:
        i = 0
        while True:
            i = i + 1
            line = f.readline()
            if not line:
                break 
            
            m1 = int(line.split(',')[0])
            m2 = int(line.split(',')[1])
            m3 = int(line.split(',')[2])

            print(f'Marks of student {i} in maths is: {m1}')
            print(f'Marks of student {i} in maths is: {m2}')
            print(f'Marks of student {i} in maths is: {m3}')



def writeListFile(ls):
    """
    This function writes the list elements to a file by line.

    Args:
        ls (list): taking list ls as argument and inserting ls element line by line
    """
    with open('#100DaysOfCode/Day50(read(), readlines() and other methods)/message3.txt', "w+") as f:
        f.writelines(ls)        



def writelistByLineFile(ls):
    """
    This function writes the list elements to a file by line

    Args:
        ls (list): taking list ls as argument and inserting ls element line by line
    """
    with open('#100DaysOfCode/Day50(read(), readlines() and other methods)/message4.txt', 'w+') as f:
        for element in ls:
            f.writelines(element)
 
 
 
def writelistByLineFile2(ls):
    """
    This function writes the list elements to a file by line, adding newline character at end after every element.

    Args:
        ls (list): taking list ls as argument and inserting ls element line by line
    """
    with open('#100DaysOfCode/Day50(read(), readlines() and other methods)/message5.txt', 'w+') as f:
        for element in ls:
            f.writelines(element + '\n')           


        
    
readlineFile()
readlineFile2()
readingArrFile()
readingArrFile2()
writeListFile(['line 1\n', 'line 2\n', 'line 3\n'])
writelistByLineFile(['line 1', 'line 2', 'line 3', 'line 4'])
writelistByLineFile2(['line 1', 'line 2', 'line 3', 'line 4'])