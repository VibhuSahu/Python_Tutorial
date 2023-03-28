Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #   Slicing and Indexing
>>> 
>>> name = "VibhuSahu"
>>> name[0]
'V'
>>> name[0:4]
'Vibh'
>>> name[:5]
'Vibhu'
>>> name[:]
'VibhuSahu'
>>> name[::]
'VibhuSahu'
>>> name[::2]
'Vbuau'
>>> name[::-1]
'uhaSuhbiV'
>>> 
>>> 
>>> 
>>> #   Concatenation
>>> "F" + name[1:]
'FibhuSahu'
>>> # adding string together
>>> letters = "PTJB"
>>> for letter in letters:
...     print(letter + name[6:])
... 
...     
Pahu
Tahu
Jahu
Bahu
