class Prostute:
    def __init__(self):     # Constructor (__init__)
        """
        When the constructor  doesn't  accept any arguments from the object and has
        Only one argument, self, in the constructor, it is known as a Default constructor.
        """
        print('Hey i am a prostituet')


class Person:
    def __init__(self, name, occupation, networth):
        """
        This class represents the person object with attributes like Name, Occupation & Net Worth
        This Function always return None

        Args:
            name (String): Name of Person
            occupation (String): Occupation of Person
            networth (int): Networth of Person
        """
        self.name = name
        self.occupation = occupation
        self.networth = int(networth) 
    
    def info(self):
        print(f'{self.name} is a {self.occupation} and Networth is {self.networth} Million')
    


a = Prostute()


a = Person('Vibhu Sahu', 'Student', 0)
b = Person('Diya', 'Student', 1)
c = Person('Rahul Dewagan', 'Camra man', 5)

a.info()
b.info()
c.info()


        
'''
Output :
Hey i am a prostituet
Vibhu Sahu is a Student and Networth is 0 Million
Diya is a Student and Networth is 1 Million
Rahul Dewagan is a Camra man and Networth is 5 Million
'''