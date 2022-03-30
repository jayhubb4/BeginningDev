name = "Jay"
if len(name) < 10:
    print("Name must be at least 10 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 charcters")
else:
    print("Name looks good!")

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")



