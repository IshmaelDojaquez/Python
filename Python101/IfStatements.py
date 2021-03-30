is_hot = False
is_cold = True

if is_hot:  # initial case
    print("It's a hot day")
    print("Drink plenty of water!")
elif is_cold:  # other case
    print("Its a cold day")
    print("Wear warm clothes")
else:  # if no other case is right
    print("It's a lovely day")

print("Enjoy your day")

# Practice
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")