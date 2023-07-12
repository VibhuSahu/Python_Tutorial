"""
Question. An athlete is taking rounds of a triangular park with side as 30 m, 25 m, and 35 m. The
          athlete has run 560 m till now. Write a program to print how many rounds of park the
          athlete has completed.

"""
def takingRoundsOfTriangle(length):
    sideA, sideB, sideC = 30, 25, 35
    perimeter = sideA + sideB + sideC
    return length // perimeter

userINput = takingRoundsOfTriangle(int(input("Enter distance you covered : ")))

print("   You completed : ", userINput, "rounds.")

"""
Ouput :
Enter distance you covered : 560
   You completed :  6 rounds.
"""