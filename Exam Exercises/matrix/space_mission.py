n = int(input())
matrix = []
spaceship_pos = []
resources = 100

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            spaceship_pos = [row, col]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
while True:
    command = input()
    r, c = spaceship_pos
    dr, dc = moves[command]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < n and 0 <= nc < n):
        print(f"Mission failed! The spaceship was lost in space.")
        break

    resources -= 5
    prev = matrix[r][c]
    tile = matrix[nr][nc]

    if tile == 'R':
        resources = min(100, resources + 10)
    elif tile == 'M':
        resources -= 5

    if tile == 'P':
        matrix[r][c] = '.' if prev == 'S' else prev
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    matrix[r][c] = '.' if prev == 'S' else prev
    matrix[nr][nc] = 'S' if tile != 'R' and tile != 'P' else tile
    spaceship_pos = [nr, nc]

    if resources < 5:
        print(f"Mission failed! The spaceship was stranded in space.")
        break

for row in matrix:
    print(*row)
