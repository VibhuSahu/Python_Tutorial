a = 123
print(a)

b = 3.45
print(b)

c = complex(8, 2)
print(c)

d = "Bibhu"
print(d)

e = None
print(e)

print("The type of a is ", type(a))
print("The type of a is ", type(b))
print("The type of a is ", type(c))
print("The type of a is ", type(d))
print("The type of a is ", type(e))


# List
list1 = [8, 2.3, [-4, 5], ['apple', 'banana']]
print(list1)
print("The type of a is ", type(list1))


# Tuple
tuple1 = ("parrot", 'sparrow', ("Lion", "Tiger"))
print(tuple1)
print("The type of a is ", tuple1)

# dictionary
dict1 = {
    "Name" : "Sakshi",
    "Age" : 28,
    "canVote" : True
}
print(dict1)
print("The type of a is ", type(dict1))


"""
Output :
    123
    3.45
    (8+2j)
    Bibhu
    None
    The type of a is  <class 'int'>
    The type of a is  <class 'float'>
    The type of a is  <class 'complex'>
    The type of a is  <class 'str'>
    The type of a is  <class 'NoneType'>
    [8, 2.3, [-4, 5], ['apple', 'banana']]
    The type of a is  <class 'list'>
    ('parrot', 'sparrow', ('Lion', 'Tiger'))
    The type of a is  ('parrot', 'sparrow', ('Lion', 'Tiger'))
    {'Name': 'Sakshi', 'Age': 28, 'canVote': True}
    The type of a is  <class 'dict'>
"""