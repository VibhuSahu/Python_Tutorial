"""
# Question. Write a program to calculate the distance of 1056 feet in terms of yards and miles. Given
            fixed values are 1 mile = 1760 yards and 1 yard = feet
"""
def feetToYard(feet):
    return feet / 3

def yardToMile(yard):
    return feetToYard(yard) / 1760


userInput = int(input(" Enter the value in feets : "))
print("    ", userInput, "feet is equal to : ", feetToYard(userInput),"yards.")
print("    ", userInput, "feet is equal to : ", yardToMile(userInput),"miles.")


"""
Output :
 Enter the value in feets : 1056
     1056 feet is equal to :  352.0 yards.
     1056 feet is equal to :  0.2 miles.
"""