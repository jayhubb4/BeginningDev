#Packages 

""" You can create directories to organize your code and reference them as you see below. Using the import method, I have pulled from another module outside of that package. 
If the __init__.py does not automatically show when you save the program, you may have to add it in yourself.
"""

import imp
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

#  Or you can do it this way, the better way.

from ecommerce.shipping import calc_shipping

# You can also import the entire module by doing this and using the "." operator

from ecommerce import shipping

shipping.calc_shipping()


# Built-in Modules
# Random Values

import random

for i in range(3):
    random.random()
print(random.random())

for i in range(3):
    random.random()
print(random.randint(10, 20))


import random

members = ['John', 'Mary', 'Bob', 'Jonathan']
leader = random.choice(members)
print(leader)

# Exercise

import random


class Dice:
    def roll(self):
        first = random,random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

# Files and Directories
# Below checks to see if path is viable and does exist
from pathlib import Path

path = Path("ecommerce")
print(path.exists())

# Below allows you to create a new directory
# Will return a Bool of 'None' but if you look it did indeed create a directory with whichever name you defined

from pathlib import Path

path = Path("emails")
print(path.mkdir())

# Below allows you to delete a directory, I will comment this out to prevent it from being removed
"""
from pathlib import Path

path = Path("ecommerce")
print(path.rmdir())

"""
# Below will show you all files and directories in a given path. Using '*.*' Means ALL files. After the first *, whatever operator you use after the '.' will deteermine which files you return

from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)



