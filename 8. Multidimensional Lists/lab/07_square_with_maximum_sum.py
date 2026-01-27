rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

max_sum = float('-inf')
sub_matrix = []
for i in range(rows - 1):
    for j in range(columns - 1):
        current = matrix[i][j]
        next_el = matrix[i][j +1]
        el_below = matrix[i + 1][j]
        el_diagonal = matrix[i + 1][j + 1]
        sum_el = current + next_el + el_below + el_diagonal
        if sum_el > max_sum:
            max_sum = sum_el
            sub_matrix = [[current, next_el], [el_below, el_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
