def code1(n):
    if (n<5 or n>9 ):
        raise ValueError("Value should be between 5 and 9.")

    return "Fuck YOu!"


print(code1(6))
print(code1(10))
print(code1(7))



"""
Output :
Traceback (most recent call last):
  File "/Users/polarbear/Documents/CodE Work/Python_tut/#100DaysOfCode/Day38(Raising custom errors in Python)/main.py", line 9, in <module>
    print(code1(10))
          ^^^^^^^^^
  File "/Users/polarbear/Documents/CodE Work/Python_tut/#100DaysOfCode/Day38(Raising custom errors in Python)/main.py", line 3, in code1
    raise ValueError("Value should be between 5 and 9.")
ValueError: Value should be between 5 and 9.
Fuck YOu!

"""
# For error - https://docs.python.org/3/tutorial/errors.html