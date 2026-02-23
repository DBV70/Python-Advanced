n = int(input())
matrix = []
pos = [0, 0]
health = 100
stars = 0
immunity = False

for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "P":
            pos = [i, j]
        if matrix[i][j] == "*":
            stars += 1

def move(position, direction, mtx):
    size = len(mtx)
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    cr, cc = position
    dr, dc = moves[direction]
    nr = (cr + dr) % size
    nc = (cc + dc) % size
    return nr, nc

while health > 0 and stars > 0:
    command = input()
    if command == "end":
        break

    row, col = pos
    matrix[row][col] = "-"
    r, c = move(pos, command, matrix)

    if matrix[r][c] == "*":
        stars -= 1
    if matrix[r][c] == "G":
        if not immunity:
            health -= 50
        else:
            immunity = False
    if matrix[r][c] == "F":
        immunity = True

    matrix[r][c] = "-"
    pos = [r, c]

r, c = pos
if health <= 0:
    print(f"Game over! Pacman last coordinates [{r},{c}]")
if stars == 0:
    print("Pacman wins! All the stars are collected.")
if health > 0 and stars > 0:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if stars > 0:
    print(f"Uncollected stars: {stars}")

matrix[r][c] = "P"
[print(''.join(row)) for row in matrix]
