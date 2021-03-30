names = ['John', 'Bob', 'Sarah', 'Mat', 'Kim']
print(names)
print(names[0])  # you can determine a specific positive or negative index
print(names[2:4])  # you can return names at a index to a given index. Does not include that secondary index
names[0] = 'Howard'

# Practice
numbers = [3, 6, 23, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
