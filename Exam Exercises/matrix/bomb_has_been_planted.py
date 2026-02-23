n, m = map(int, input().split(', '))
matrix = []
time = 16
pos = [0, 0]
start_pos = [0, 0]
defuse_ready = False

for i in range(n):
    matrix.append(list(input()))
    for j in range(m):
        if matrix[i][j] == "C":
            start_pos = [i, j]
            pos = start_pos

def move(position, direction):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    dr, dc = moves[direction]
    return position[0] + dr, position[1] + dc

while time > 0:
    row, col = pos
    command = input()
    if command == "defuse":
        if not defuse_ready:
            time -= 2
            continue
        if time >= 4:
            matrix[row][col] = 'D'
            time -= 4
            break
        matrix[row][col] = 'X'
        time -= 4
        break

    matrix[row][col] = "*" if matrix[row][col] != "B" else "B"
    r, c = move(pos, command)
    time -= 1
    if 0 <= r < n and 0 <= c < m:
        pos = [r, c]
        if matrix[r][c] == "B":
            defuse_ready = True
            continue
        if matrix[r][c] == "T":
            matrix[r][c] = "*"
            break
        defuse_ready = False

if time == 0 or any('X' in row for row in matrix):
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(time)} second/s.")
elif any('D' in row for row in matrix):
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time} second/s remaining.")
else:
    print("Terrorists win!")

r, c = start_pos
matrix[r][c] = "C"
[print(''.join(row)) for row in matrix]
