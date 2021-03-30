i = 1
while i <= 5:  # will continue to loop as long as the statement is true
    print('*' * i)  # this will multiple the string by the int. Producing '**'
    i += 1

print("Done")

# Practice
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
    else:
        print('Sorry, you failed!')

