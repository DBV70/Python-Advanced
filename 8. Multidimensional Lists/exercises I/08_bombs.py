n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()

for bomb in bombs:
    b_row, b_col = map(int, bomb.split(','))
    b_value = matrix[b_row][b_col]
    if b_value > 0:
        matrix[b_row][b_col] = 0
        for r in range(b_row - 1, b_row + 2):
            for c in range(b_col - 1, b_col + 2):
                if 0 <= r < n and 0 <= c < n:
                    if matrix[r][c] > 0:
                        matrix[r][c] -= b_value

alive_cells = len([col for row in matrix for col in row if col > 0])
cells_sum = sum([col for row in matrix for col in row if col > 0])

# alive_cells = 0
# cells_sum = 0
# for row in matrix:
#     for col in row:
#         if col > 0:
#             alive_cells += 1
#             cells_sum += col

print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")
[print(*row) for row in matrix]
