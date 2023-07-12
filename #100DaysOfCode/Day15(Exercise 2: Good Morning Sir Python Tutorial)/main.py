from time import strftime

def wish():
    # hour variable time in 24 hour frame
    hour = int(strftime("%I"))

    # wish u according hour variable.
    if (4 <= hour and hour < 12):       # Good morning
        print(" Good morning! \n sir. ")
    elif (12 <= hour and hour < 17):    # Good afternoon
        print(" Good afternoon! \n sir. ")
    elif (17 <= hour and hour < 20):    # Good evening
        print(" Good evening! \n sir. ")
    else:       # Good night
        print(" Good night! \n sir.")


# Function call
wish()


"""
Output :
 Good morning! 
 sir. 
"""