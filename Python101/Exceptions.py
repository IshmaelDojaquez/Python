try:  # place what you are testing in the try section
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:  # can catch multiple exceptions
    print('Invalid Error')


