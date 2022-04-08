""" 

Dictionaries; 
They can store key value pairs. Each key must be unique and when trying to print or reference, it must match the exact value with capitalization and all. It can be literally anything also,
strings, ints, anything


"""
customer = { 
    "name": "Jonathan Hubbard",
    "age" : 30,
    "is_verified": True

}
print(customer["name"])
print(customer.get("birthdate", "Oct 29 1990"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "?!") + " "

print(output)

"""

Emoji Converter

"""

message = input(">")
words = message.split(' ')
print(words)

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😂",
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)



"""

Functions

"""

def greet_user():
    print("Hit there!")
    print('Welcome aboard!')

print("Start")
greet_user()
print("Finish")

"""

Parameters

"""
def greet_user(name):
    print("Hi there!")
    print('Welcome aboard!')

print("Start")
greet_user("")
print("Finish")

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')

print("Start")
greet_user("Jonathan")
print("Finish")

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')

print("Start")
greet_user("Jonathan")
greet_user("Charday")
print("Finish")

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')

print("Start")
greet_user("Jonathan")
print("Finish")




"""

Keyword Arguments

"""

def greetings(first, last):
    print(f'Hi {first} {last}!')
    print('Welcome!')

print("Start")
greetings(last = "Hubbard", first = "Jonathan")
calc_cost(total = 50, shipping = 5, discount = 0.1)
print("Done")





"""

Return Statements

"""

def square(number):
    return number * number


result = square(3)
print(result)


def square(number):
    return number * number


print(square(3))




def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😂",
        ":(": "😒"
}
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))









