age = int(input('Age: '))
print(age)

""" Exit code '0' means program completed successfully, anything but 0 means the program crashed 

'try except' method handles errors and can be used to display the proper error message"""

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be 0.')

#You can use this sign to signify a comment as well

#CLASSES
#In variables, keep everything lowercase, but in classes, use the Pascal naming convention by capitalizing the first letter of every word

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()



#New example
point1 = Point()
point1.x = 10
point1.y = 20 
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)




#Constructor
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")
point = Point(10, 20)
print(point.x)





#Exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()


#Inheritance


class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()


#Modules
#Modules are organized files in coding. So, If you have a function in another Module (like this one is called Exceptions), you can call it

from email import message
import Dictionaries_and_misc
from Dictionaries_and_misc import emoji_converter

print(Dictionaries_and_misc.emoji_converter(message))


#Exercise
from Utilities import find_max

numbers = [10, 3, 6, 2]
max = find_max(numbers)
print(max)


