is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("""Drink plenty of water,
    Wear sunscreen,
    and Go to the beach!
    
    """)
elif is_cold: 
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")


home_price = int(1000000)
GCdown_payment = home_price * 0.10
BCdown_payment = home_price * 0.20
good_credit = True

if good_credit:
    down_payment = GCdown_payment
else:
    down_payment = BCdown_payment
print(down_payment)
print(f"Down Payment: ${down_payment}")

High_Income = True
Good_Credit = True
OK_Credit = True
criminal_rec = False


if High_Income and Good_Credit:
    print('eligible')

if High_Income or OK_Credit:
    print('eligible')

if High_Income and not criminal_rec:
    print('eligible')

name = "J"
print(len(name))
if len(name) < 3:
    print("Name must be at least 3 charcters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else: print("Looks Good!")