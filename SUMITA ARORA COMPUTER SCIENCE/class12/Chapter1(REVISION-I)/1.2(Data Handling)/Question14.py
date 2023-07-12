"""
# Question. Write a Python program that calculates and prints on the screen the number of seconds in a year.
    1 year = 365 days
    1 days = 24 hours
    1 hours = 60 minutes
    1 minutes = 60 seconds
"""

def yearToSeconds(yearNum):
    sumOfSeconds = 60 * 60 * 24 * 365
    return yearNum * sumOfSeconds

numYear = int(input(" Number of Year : "))
print("    ", numYear, "year  have ",yearToSeconds(numYear),"seconds.")

"""
Output :
 Number of Year : 2
     2 year  have  63072000 seconds.
"""