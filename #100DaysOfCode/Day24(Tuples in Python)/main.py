>>> tup1 = (1, 5, 6)
>>> print(type(tup1))
<class 'tuple'>
>>> print(type(tup1), tup1)
<class 'tuple'> (1, 5, 6)
>>>
>>> tup2 = (1)
>>> tup3 = (1,)
>>> print(type(tup2), tup2)
<class 'int'> 1
>>> print(type(tup3), tup3)
<class 'tuple'> (1,)
>>>
>>> tup4 = (1, 2, 76, 342, 32)
>>> tup4
(1, 2, 76, 342, 32)
>>> tup4[0] = 90
Traceback (most recent call last):
  File "/Users/polarbear/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-C/ch-0/231.9011.38/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> tup5 = (1, 2, 76, 342, 32, "green", True)
>>> tup5
(1, 2, 76, 342, 32, 'green', True)
>>> tup[0]
Traceback (most recent call last):
  File "/Users/polarbear/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-C/ch-0/231.9011.38/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
NameError: name 'tup' is not defined. Did you mean: 'tup1'?
>>> tup5[0]
1
>>> tup5[1]
2
>>> tup5[2]
76
>>> tup5[3]
342
>>> tup5[4]
32
>>> tup5[5]
'green'
>>> tup5[6]
True
>>> tup5[36]
Traceback (most recent call last):
  File "/Users/polarbear/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-C/ch-0/231.9011.38/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
>>>
>>> if 32 in tup5:
...     print(" Yes ")
...
 Yes
>>>
>>> if 35 in tup5:
...     print("Yes")
...
>>>
>>> tup5[1:4]
(2, 76, 342)
>>> tup5[:]
(1, 2, 76, 342, 32, 'green', True)
>>> tup5[:3]
(1, 2, 76)
>>> tup5[:5:2]
(1, 76, 32)