course = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(course)

'(*********Indexes************)'

course = 'Python for Beginners'
print(course[-2])
print(course[0:3])
print(course[0:])
print(course[:3])
another = course[:]

name = 'Jennifer'
print(name[1:-1])


'(*********Formatted strings************)'
first = 'Jonathan'
last = 'Hubbard'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())

print(course.find('P'))
print(course.find('Beginners'))

print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('P','J'))

print('Python' in course)
print('python' in course)

name = 'john doe'.title()
print(name)