import os

def presentWorkingDirectory():
    """
    This function returns the current directory of your system

    Returns:
        _type_: output will be string
    """
    PWD = os.getcwd()
    return f"Current working on : {PWD}"


def createFolder(name):
    """
    this function create folder in your directory

    Args:
        name (string): it is folder name by which the folder get created.
    """
    os.mkdir(f"/Users/polarbear/Documents/CodE Work/Python_tut/#100DaysOfCode/Day46(os Module in Python)/{name}")
    print(" Successful! \n")
    
    
def createFolderNOCHANGE(folder):
    """
    It creates a new empty folder and at last path will be home path

    Args:
        folder (string): Name of folder which is going to create
    """
    os.chdir("/Users/polarbear/Documents/CodE Work/Python_tut/#100DaysOfCode/Day46(os Module in Python)")
    os.mkdir(folder)
    os.chdir(os.path.expanduser("~"))
    print(" Successful! \n")
    

def creating10File(folder, name):
    """
    It create a folder and another 10 folder inside it.

    Args:
        folder (string): Name of parent folder
        name (string): Name of child folder
    """
    os.chdir('/Users/polarbear/Documents/CodE Work/Python_tut/#100DaysOfCode/Day46(os Module in Python)')
    os.mkdir(folder)
    for i in range(10):
        PWD = name + str(i+1) 
        os.mkdir(os.path.join(folder,PWD))
    print(" Successful! \n")
    
def whereIsFile():
    """
    It will return the path of current file

    Returns:
        string : current path of file 
    """
    return os.path.abspath(__file__)
    
def creating10FileWithTXT(folder, file, txt):
    """
    Creating 10 folder inside a folder and inside those 10 folder creating txt file 

    Args:
        folder (string): Name of parent folder
        file (string): Name child folder
        txt (string): Name txt file which is going to be inside child folder
    """
    pass
    
    
    
    



# print(presentWorkingDirectory())
# createFolder("data")
# createFolderNOCHANGE("hello")
# creating10File('tut', 'day')
# print(whereIsFile())
# creating10FileWithTXT("PythonTUT", "Topic", "main.py")