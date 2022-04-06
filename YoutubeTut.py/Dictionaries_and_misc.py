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
print(customer.get("birthdate", "Jan 1 1980"))

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


