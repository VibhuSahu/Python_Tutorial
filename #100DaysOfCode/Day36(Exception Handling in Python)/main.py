def code1(a):
    print(f"Multiplication table of {a} is : ")

    try:
        for i in range(1, 11):
            print(f"{int(a) } X {i} = {int(a) * i}")
    except Exception as e:
        print(e)

    print("Some imp lines of code")
    print("End of program")
    print("\n")


def code2(a):
    print(f"Multiplication table of {a} is : ")

    try:
        for i in range(1, 11):
            print(f"{int(a) } X {i} = {int(a) * i}")
    except Exception as e:
        print("sorry! some error occurred")

    print("Some imp lines of code")
    print("End of program")
    print("\n")


def code3(a):
    print(f"Multiplication table of {a} is : ")

    try:
        for i in range(1, 11):
            print(f"{int(a) } X {i} = {int(a) * i}")
    except:
        print("Invalid Input!")

    print("\n")


def code4(num):
    try:
        num = int(num)
        a = [6, 3]
        print(a[num])
    except ValueError:
        print("Number entered is not an integer.")
    except IndexError:
        print("Index Error!")




code1(7)
code1("7")
code1("vibhu")

code2("vibhu")

code3("vibhu")


code4(1)
code4(5)
code4('ad')


"""
Output :
Multiplication table of 7 is : 
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
Some imp lines of code
End of program


Multiplication table of 7 is : 
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
Some imp lines of code
End of program


Multiplication table of vibhu is : 
invalid literal for int() with base 10: 'vibhu'
Some imp lines of code
End of program


Multiplication table of vibhu is : 
sorry! some error occurred
Some imp lines of code
End of program


Multiplication table of vibhu is : 
Invalid Input!


3
Index Error!
Number entered is not an integer.

"""