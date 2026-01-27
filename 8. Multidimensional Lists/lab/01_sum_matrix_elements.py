rows, column = [int(x) for x in input().split(', ')]
matrix = []
total = 0
for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)
    total += sum(data)

print(total)
print(matrix)

# total_a = 0
# matrix_a = [[int(x) for x in input().split(', ')] for _ in range(rows)]
# for row in matrix_a:
#     total_a += sum(row)
#
# print(total_a)
# print(matrix_a)
