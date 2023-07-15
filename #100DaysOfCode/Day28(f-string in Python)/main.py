letter = "Hey my name is {} and I am from {}"
Letter = "Hey my name is {1} and I am from {0}"

country = "India"
name = "Vibhu"
price = 49.09999

print(letter.format(name, country))
print(letter.format(country, name))

print(Letter.format(country, name))
print(Letter.format(name, country))


print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


txt = "For only {price: .2f} dollars!"
print(txt.format(price = 59.34229))


print(f"For only {price: .2f} dollars!")
print(type(f"{2 * 30}"))


"""
Output :
Hey my name is Vibhu and I am from India
Hey my name is India and I am from Vibhu
Hey my name is Vibhu and I am from India
Hey my name is India and I am from Vibhu
Hey my name is Vibhu and I am from India
We use f-strings like this: Hey my name is {name} and I am from {country}
For only  59.34 dollars!
For only  49.10 dollars!
<class 'str'>

"""