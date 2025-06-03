matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


matrix[0][1] = 20
print(
matrix
)

matrix[0][1] = 2
for row in matrix:
    for column in row:
        print(column)