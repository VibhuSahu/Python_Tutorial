
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    print("\n")


def GreaterThan(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

    print("\n")


def isLesser(a, b):
    pass  # Pass tells Python to skip this line and do nothing


# Part 1
a, b, c, d = 9, 8, 7, 8

calculateGmean(a, b)   # Function call
calculateGmean(c, d)

# Part 2
GreaterThan(a, b)
GreaterThan(c, d)


# Part 3
isLesser(a, b)
isLesser(c, d)



"""
Output :
4.235294117647059


3.7333333333333334


First number is greater


Second number is greater or equal



"""