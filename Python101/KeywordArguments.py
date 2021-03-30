def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Paul")  # referred to as positional arguments... meaning their position or order matters
greet_user("Mary", "Little")  # fist_name = Mary and last_name = Little
greet_user(last_name="Billy", first_name="Bob")  # keyword arguments do not matter about position.
greet_user("Billy", first_name="Bob")  # Keyword arguments must go after positional arguments
print("Finish")