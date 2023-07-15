s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

nums1 = {1, 2, 3, 4, 5}
nums2 = {6, 7, 8, 9, 0}
nums3 = {1, 2, 3, 4, 5}


print(s1.union(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.intersection(s2))

nums1.update(nums2)
print(nums1)
print(nums2)


print(s1.isdisjoint(s2))
print(nums3.isdisjoint(nums2))


print(nums1.issuperset(nums2))
print(nums2.issuperset(nums3))
print(nums1.issubset(nums2))
print(nums2.issubset(nums3))


# Adding element
nums1.add(10)
nums1.add(11)
print(nums1)


# removing the element
nums1.remove(10)        # if n not present inside it will though error
nums1.discard(11)       # if n not present inside it will not though error
nums1.pop()             # removing last element from set

print(nums1)

del nums1               # nums1 is deleted

if 7 in nums2:
    print("Carla is present.")
else:
    print("Carla is absent.")

"""
Output :
{1, 2, 3, 5, 6, 7}
{1, 2, 5}
{3, 7}
{6}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 6, 7, 8, 9}
False
True
True
False
False
False
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
Carla is present.
"""