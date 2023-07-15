eq1 = {122: 45, 123: 89, 567: 69, 670: 69}
eq2 = {222: 67, 566: 98}
empt = {}
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}



eq1.update(eq2)    # Adding eq2 element in eq1
print(eq1)

eq1.clear()        # removing all element in dic
print(eq1)

print(empt)
print(type(empt))


eq2.pop(222)       # removing 222 in eq2
print(eq2)

eq2.popitem()
print(eq2)

del eq2            # it will delete eq2
del person['age']

print(person)


"""
Output :
{122: 45, 123: 89, 567: 69, 670: 69, 222: 67, 566: 98}
{}
{}
<class 'dict'>
{566: 98}
{}
{'name': 'John Doe', 'city': 'New York', 'occupation': 'Engineer'}

"""