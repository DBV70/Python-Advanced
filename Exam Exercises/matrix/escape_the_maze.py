n = int(input())
maze = []
health = 100
pos = [0, 0]

for row in range(n):
    maze.append(list(input()))
    for col in range(n):
        if maze[row][col] == "P":
            pos = [row, col]

def move(position, direction):
    r, c = position
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    dr, dc = moves[direction]
    new_row, new_col = r + dr, c +dc
    return new_row, new_col

while True:
    command = input()
    maze[pos[0]][pos[1]] = "-"
    nr, nc = move(pos, command)
    if 0 <= nr < n and 0 <= nc < n:
        pos = [nr, nc]
        if maze[nr][nc] == "M":
            maze[nr][nc] = "-"
            health = max(0, health - 40)
            if health <= 0:
                print("Player is dead. Maze over!")
                break

        if maze[nr][nc] == "H":
            health = min(100, health + 15)
            maze[nr][nc] = "-"

        if maze[nr][nc] == "X":
            maze[nr][nc] = "-"
            print("Player escaped the maze. Danger passed!")
            break
    else:
        continue

print(f"Player's health: {health} units")
maze[pos[0]][pos[1]] = "P"
[print("".join(row)) for row in maze]
