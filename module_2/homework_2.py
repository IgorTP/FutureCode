arr_shape = (3, 3)
rows, cols = arr_shape

matrix = [
    [0 for _ in range(cols)]
    for _ in range(rows)
]

num = 1
for row in range(rows):
    for col in range(cols):
        matrix[row][col] = num
        num += 1

for row in matrix:
    print(row)
