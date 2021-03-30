course = 'Python for "Beginners"'  # using "" will allow the us of ' and vice versa
print(course)

new_course = '''
Hi John,

Here is your first email to you

Thank you,
The Support Team


'''  # use triple " or triple ' to write a paragraph worth

print(course[0])  # you can use indexing to get specific characters of a string
print(course[-1])  # in python you can use negative indexing
print(course[0:3])  # starts at the index declared and goed to the index prior of what is declared
#  python will assume the start and end idex if it is left empty

# Practice
name = 'Jennifer'
print(name[1:-1])  # will print from index 1, which is 'e' all the way to index -1, which is 'e'
