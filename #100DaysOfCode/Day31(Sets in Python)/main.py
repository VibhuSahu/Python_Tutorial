# Set in Python
# Set - Set is a collection of well defined objects.
#       set is collection of elements in unordered manera
#       set doesn't have duplicate elements


set = {2, 4, 2, 6}
box = {"Carla", 19, False, 5.9, 19}

print(set)
print(box)
print(*box)

for element in box:
    print(element)


"""
Output :
{2, 4, 6}
{False, 19, 5.9, 'Carla'}
False 19 5.9 Carla
False
19
5.9
Carla
"""