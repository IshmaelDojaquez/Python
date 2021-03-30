weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")

if unit.upper() == "L":
    converted = weight * .45
    print(f"You are {converted} kilos")
else:
    converted = weight / .45
    print(f"You are {converted} pounds")

