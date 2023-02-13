khaali_list = []                       # Empty List

lst_1 = ['one','two','three','four']   # List of strings
lst_2 = ['1','2','3','4']              # List of integers
lst_3 = [[1,2],[3,4]]                  # List of lists
lst_4 = [1,'chintu',12,1.5]            # List of different datatypes

print(lst_4)                           # How we print any list

print(len(lst_1))                      # Find Length of list (4)

lst_1.append("five")                   # Append will add the item at the end
print(lst_1)                           # ['one', 'two', 'three', 'four', 'five']

lst_1.remove('three')                  # It will remove first occurence of two in a given list
print(lst_1)                           # ['one', 'two', 'four', 'five']

lst_1.insert(2,'three')                # Insert will add element y at location x
print(lst_1)                           # ['one', 'two', 'three', 'four', 'five']


lst_1.append(lst_2)                    # Append will add list as it's
print(lst_1)                           # ['one', 'two', 'three', 'four', 'five', ['1', '2', '3', '4']]

lst_4.extend(lst_2)                    # Extend will put all element of list a inside b list
print(lst_4)                           # [1, 'chintu', 12, 1.5, '1', '2', '3', '4']

del lst_4[0]                           # it is use delete any value with index number
print(lst_4)                           # ['chintu', 12, 1.5, '1', '2', '3', '4']

a = lst_4.pop()                        # It is use the eleminate
print(a)                               # ['chintu', 12, 1.5, '1', '2', '3', '4']
print(lst_4)                           # ['chintu', 12, 1.5, '1', '2', '3']

lst_4.reverse()                        # It to reverse all the values
print(lst_4)

# sorted function only we use in copy of any list
numbers = [3,1,6,2,8]
sorted_list = sorted(numbers)
print("Sorted list : ", sorted_list)   # Sorted list :  [1, 2, 3, 6, 8]

print("Original List : ",numbers)      # Sorted list :  [1, 2, 3, 6, 8]

reversed_sorted_list = sorted(numbers,reverse=True)         # It will sort and reverse the order
print(reversed_sorted_list)                                 # [8, 6, 3, 2, 1]
print(numbers)                                              # Original remains the same


numbers.sort()                           # It help you to sort the list only for list contan integers
print("Sorted list : ",numbers)          # Sorted list :  [1, 2, 3, 6, 8]

