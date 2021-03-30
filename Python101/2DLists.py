# [1 2 3]
# [4 5 6]
# [7 8 9]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20  # changing a value at a specific index
print(matrix[0][1])  # printing a specific index value

# iterate through the whole matrix
for row in matrix:
    for item in row:
        print(item)
