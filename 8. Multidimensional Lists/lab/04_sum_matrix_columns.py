rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col in range(columns):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)
