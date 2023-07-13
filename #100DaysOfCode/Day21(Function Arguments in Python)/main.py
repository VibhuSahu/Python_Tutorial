
def average(a=9, b=1):
    print("The average is ", (a+b)/2)



def averageValue(a, b, c=1):
    print("The average is ", (a + b + c) / 2)



def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)



def averageList(*nums):
    lslen = len(nums)
    lsSum = sum(nums)
    print("Average is: ", (lsSum/lslen))




average(4, 6)           # Part 1
average(b=9)            # Part 2
average(b=9, a=21)      # Part 3

averageValue(5, 6)      # Part 4


name("Amy","Agarwal")           # Part 5
name("Amy", "Agarwal", "Jain")  # Part 6

averageList(1,2,3,4,5,6,7,8,9)  # Part 7



"""
Output :
The average is  5.0
The average is  9.0
The average is  15.0
The average is  6.0
Hello, Amy Agarwal Whatson
Hello, Amy Agarwal Jain
Average is:  5.0
"""