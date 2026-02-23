n = int(input())
matrix = []
bunny = []
eggs = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny = [row, col]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_eggs = float("-inf")
max_direction = ""
max_mat = []

for direction, move in moves.items():
    eggs = 0
    current_mat = []
    row, col = bunny[0] + move[0], bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break
        eggs += int(matrix[row][col])
        current_mat.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_mat:
        max_eggs = eggs
        max_direction = direction
        max_mat = current_mat

print(max_direction)
for row in max_mat:
    print(row)
print(max_eggs)
