"""
# Question. Write a program that prints a table on two columns: on the left the integer temperatures
            between 0 and 100(Fahrenheit) and it the right column the corresponding Celsius values.

            C = (F - 32) x 5 / 9
            F = C x (9 / 5) + 32
"""
def fahrenheitToCelsius(temp):
    return (temp - 32) * (5 / 9)

for x in range(0,101):
    print(f"   Temperatures in Fahrenheit is {x:3} F,  And in Celsius is {fahrenheitToCelsius(x):4.2f} C")