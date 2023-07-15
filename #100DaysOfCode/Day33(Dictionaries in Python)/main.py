# Creating a dictionary
dic = {
    344: "Vibhu",
    56: "Shahabaz",
    678: "Harsh",
    567: "Neha"
}
info = {'name':'Karan', 'age':19, 'eligible':True}



print(dic[567])
print(info['name'])
print(info.get('eligible'))     # fatching out value from dictionary if element is not present it will not throught error
print(info.get('Hello'))
print()

print(info.keys())


for key in info.keys():
    print(info.get(key))


for value in dic.values():
    print(f"The Value is {value}.")

for key, value in dic.items():
    print(f"The key of {value} is {key}")


"""
Output :
Neha
Karan
True
None

dict_keys(['name', 'age', 'eligible'])
Karan
19
True
The Value is Vibhu.
The Value is Shahabaz.
The Value is Harsh.
The Value is Neha.
The key of Vibhu is 344
The key of Shahabaz is 56
The key of Harsh is 678
The key of Neha is 567

"""