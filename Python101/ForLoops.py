for item in 'Python':  # in this example... the for loop goes through each letter of the string
    print(item)

for item in ['John', 'Sarah', 'Bill']:  # in this example... the for loop will iterate through each name in the list
    print(item)

for item in range(5, 10, 2):  # start point, stop point, amount skipped
    print(item)

# Practice
prices = [10, 20, 30]
sum = 0
for price in prices:
    sum += price
print(f"Total: {sum}")