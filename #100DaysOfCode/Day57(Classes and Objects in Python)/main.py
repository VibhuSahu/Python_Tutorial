class Person:
    name = "Vibhu"
    occupation = "Software Developer"
    networth = 10
    
    def info(self):
        print(f'{self.name} is a {self.occupation} and Networth is {self.networth} Million')
    


    
a = Person()
print(a)
print(a.name)
print(a.occupation)


# Changing character info
a.name = "Shubham"
a.networth = "Web Developer"
a.networth = 8

a.info()


# Making another Character
b = Person()
b.name = "Nitika"
b.occupation = "HR"
b.networth = 25
b.info()


"""
Output :
<__main__.Person object at 0x102ed5fd0>
Vibhu
Software Developer
Shubham is a Software Developer and Networth is 8 Million
Nitika is a HR and Networth is 25 Million
"""