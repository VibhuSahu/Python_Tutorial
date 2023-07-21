def findTheFIleType():
    """
    Finding out type of variable f.
    """
    with open("#100DaysOfCode/Day51(seek(), tell() and other functions)/message1.txt", "a+") as f:
        print(type(f))  # <class '_io.TextIOWrapper'>
        


def usingSeekFile():
    """
    Using seek function on a text file and swifting cursor and reading element. 
    """
    f = open('#100DaysOfCode/Day51(seek(), tell() and other functions)/message2.txt', 'r')
    
    # Move to the 4th Byte in the file
    f.seek(4)
    
    # Read the next 5 bytes
    data = f.read(5)
    print(data)         # 45678



def usingTellFile():
    """
    Using tell function on a text file, finding current position of cursor.
    """
    with open('#100DaysOfCode/Day51(seek(), tell() and other functions)/message2.txt', 'r') as f:
        f = open('#100DaysOfCode/Day51(seek(), tell() and other functions)/message2.txt', 'r')
    
    # Move to the 4th Byte in the file
    f.seek(4)
    
    # tell() is use to find cursor location
    print(f.tell())     # 4
    
    # Read the next 5 bytes
    data = f.read(5)
    print(data) 
    
    

def usingTruncateFile():
    """
    Truncating files by setting size smaller than or equal to its original length will remove all contents
    """
    with open('#100DaysOfCode/Day51(seek(), tell() and other functions)/message3.txt', 'w') as f:
        f.write('Hello, World3!')
        f.truncate(6)
        
    with open('#100DaysOfCode/Day51(seek(), tell() and other functions)/message3.txt', 'r') as f:
        print(f.read())
    
    
    
    
findTheFIleType()
usingSeekFile()
usingTellFile()
usingTruncateFile()