user1 = int(input(" Enter any number : "))

match user1:
    case 0:
        print(" Zero ")
    case 1:
        print(" One ")
    case 2:
        print(" Two")
    case 3:
        print(" Three ")
    case 4:
        print(" Four ")
    case 5:
        print(" Five ")
    case 6:
        print(" Six ")
    case 7:
        print(" Seven ")
    case 8:
        print(" Eight ")
    case 9:
        print(" Nine")
    case _:
        print(" Greater than 9!")


x = int(input(" Enter another Number : "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

"""
Output :
 Enter any number : 3           # input
 Three 
 Enter another Number : 80      # input
80 is not 90
"""