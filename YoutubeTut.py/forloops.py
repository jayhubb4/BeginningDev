

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


