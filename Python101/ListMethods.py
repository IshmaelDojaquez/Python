numbers = [5, 2, 1, 7 ,4, 5]
numbers.append(20)  # adds a number to the end
numbers.insert(0, 10)  # adds at a specific index
numbers.remove(5)
numbers.clear()
numbers.pop()  # removes the number from the end of the list
numbers.count(5)  # will give you the count of that specific value appearing
numbers.sort()  # sorts the list
numbers.reverse()  # reverse the list
numbers2 = numbers.copy()  # copies all the values within the list
numbers2.append(10)  # will only affect the second list and not the first

# Practice
numbers3 = [2, 2, 4, 6, 3, 4, 6, 1]
for number in numbers3:
    occurs = numbers3.count(number)
    if occurs > 1:
        numbers3.remove(number)
print(numbers3)
