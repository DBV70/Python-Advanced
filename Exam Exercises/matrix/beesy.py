n = int(input())
matrix = []
bee_pos = [0, 0]
bee_energy = 15
bee_nectar = 0
min_nectar = 30
bee_lives = 1

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'B':
            bee_pos = [row, col]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Simulates bee movement; updates energy, nectar, and matrix
while True:
    command = input()
    row, col = bee_pos
    dr, dc = moves[command]
    r = (row + dr) % n
    c = (col + dc) % n
    bee_energy -= 1
    bee_pos = [r, c]
    matrix[row][col] = '-'

    if matrix[r][c].isdigit():
        bee_nectar += int(matrix[r][c])

    if matrix[r][c] == 'H':
        if bee_nectar >= min_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0:
        if bee_nectar < min_nectar or bee_lives <= 0:
            print("This is the end! Beesy ran out of energy.")
            break
        bee_energy = bee_nectar - min_nectar
        bee_nectar = min_nectar
        bee_lives -= 1

matrix[r][c] = 'B'
[print(''.join(row)) for row in matrix]
