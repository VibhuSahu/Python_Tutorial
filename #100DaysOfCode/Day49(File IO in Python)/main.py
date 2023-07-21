def JustToWhatItPrints():
    f = open('#100DaysOfCode/Day49(File IO in Python)/message1.txt', 'r')
    print(f)
    f.close()
    print('\n')



def readingFile():
    """
    This function reads the contents of a file and prints it to console
    """
    f = open('#100DaysOfCode/Day49(File IO in Python)/message1.txt', 'r')
    text = f.read()
    print(text)
    f.close()
    print('\n')
    
  
    
def WritingFile(userWriter):
    """
    Writes user input into message2.txt
    -> if some thing is already in the file it will erase it and write it again
    -> if file not present it get's created.
    
    Args:
        userWriter (string): string para to insert in txt file.
    """
    with open('#100DaysOfCode/Day49(File IO in Python)/message2.txt', 'w') as f:
        f.write(userWriter)
        
        
        
def AppendFile(userWriter):
    """
    Appends new line at end of existing content
    -> if file not present it get's created.
    -> it will add contant after text already present.

    Args:
        userWriter (string): string para to insert in text file.
    """
    with open('#100DaysOfCode/Day49(File IO in Python)/message3.txt', 'a') as f:
        f.write(userWriter)
        f.write('\n')
    
    
 
    
# Reading file type and file contant inside 
JustToWhatItPrints()
readingFile()


# Writing text variable contant in file message2.txt
text = """The exam days are the most critical part of a students life.
It is a time when the students academic skills are put to the test and
they are under immense pressure to perform well. The examination period 
can be very stressful for students, as they have to juggle their 
studies with their other commitments.
"""
WritingFile(text)


# Appending text contant after text present already present.
AppendFile(text)