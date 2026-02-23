n = int(input())
matrix = []
pos = [0, 0]
armor = 300
enemies = 4

for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "J":
            pos = [i, j]

def move(position, direction):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    dr, dc = directions[direction]
    nr, nc = pos[0] + dr, pos[1] + dc
    return nr, nc

while armor > 0 and enemies > 0:
    command = input()
    row, col = pos
    matrix[row][col] = "-"
    r, c = move(pos, command)
    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "E":
            armor -= 100
            enemies -= 1

        if matrix[r][c] == "R":
            armor = 300

        matrix[r][c] = "-"
        pos = [r, c]

row, col = pos
if enemies == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")

matrix[row][col] = "J"
[print("".join(row)) for row in matrix]
