# birth_year = input('Birth Year: ')  will receive input as a string and therefore needs to be converted to int
birth_year = input('Birth Year: ')
age = 2021 - int(birth_year)  # converts the string to an int using int()
print(age)

# Practice
weight_lbs = input('Weight (lbs): ')
weight_kgs = int(weight_lbs) * 0.45
print (weight_kgs)
