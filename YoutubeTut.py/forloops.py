

import numbers


for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
        print(item)

for number in range(10):
    print(number)

for number in range(5, 10):
    print(number)

for number in range(5, 10, 2):
    print(number)

prices = [10, 20, 30]
total = 0
for number in prices:
    total += number
print(f"Total: {total}")


"""
Nested Loops

"""

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

"""
This is an easy way to return this:
xxxxx
xx
xxxxx
xx
xx
But is considered cheating, but also good food for thought
"""

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

"""
This is the correct way to return this:
xxxxx
xx
xxxxx
xx
xx
"""
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers = [2, 2, 2, 2, 8]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

"""
Lists

"""
names = ['John', 'Bob', 'Charday']
print(names)

names = ['John', 'Bob', 'Charday']
print(names[0])

names = ['John', 'Bob', 'Charday']
print(names[2])

names = ['John', 'Bob', 'Charday']
print(names[-1])

names = ['John', 'Bob', 'Charday']
print(names[0])

names = ['John', 'Bob', 'Charday']
print(names[2:])

names = ['John', 'Bob', 'Charday']
print(names[1:2])

names = ['John', 'Bob', 'Charday']
names[0] = 'Jon'
print(names)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

"""

2D Lists

"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)


"""
This is how to remove duplicates in a list

"""
digits = [8, 8, 3 , 6, 12, 20, 33, 12, 9]
uniques = []
for number in digits:
    if number not in uniques:
        uniques.append(number)
print(uniques)

"""

Tuples (Lists that cannot be modified or are immutabale.
To use this, place your list in parentheses instead of brackets. You will notice that you will only be able to use two methods with this, count and index. Count returns the number of occurances, 
and index returns its place in the list, or tuple.

"""

numbers = (1, 2, 3)

"""

Unpacking

"""

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates

"""

Python will take each variable and assign the number to it sequentially inside the tuple. So, Line 165 is the same as lines 161 - 163 just more concise. This is called unpacking and its is not limited to 
tuples, it can be used with regular lists (square brackets) as well.

"""


