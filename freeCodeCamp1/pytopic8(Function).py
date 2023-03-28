#   Function


# 'def' keyword is use to difine a function.
def hello():
    print('hello')


# 'sep' is used to change the default spacing with something else
def helloName(name):
    print('Good morning', name,sep=' ')


# input function use for taking input from user
hello()
helloName(input("Enter your name : "))


# You can use function inside a function

def blank():
    print()

def blank_3():
    blank()
    blank()
    blank()

def blank_9():
    blank_3()
    blank_3()
    blank_3()


blank_9()



# recursion - it means a defined function can call itself
