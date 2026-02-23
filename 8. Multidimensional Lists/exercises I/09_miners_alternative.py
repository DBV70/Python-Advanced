field_size = int(input())
commands = input().split()
field = [input().split() for _ in range(field_size)]

miner_r, miner_c = next(
    (r, c)
    for r in range(field_size)
    for c in range(field_size)
    if field[r][c] == "s"
)
total_coal = sum(cell == 'c' for row in field for cell in row)

moves = {
    "left": (0, - 1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for command in commands:
    dr, dc = moves[command]
    new_r, new_c = miner_r + dr, miner_c + dc

    if not (0 <= new_r < field_size and 0 <= new_c < field_size):
        continue

    miner_r, miner_c = new_r, new_c
    cell = field[new_r][new_c]

    if cell == 'e':
        print(f"Game over! ({new_r}, {new_c})")
        break

    elif cell == 'c':
        total_coal -= 1
        field[new_r][new_c] = '*'
        if total_coal == 0:
            print(f"You collected all coal! ({new_r}, {new_c})")
            break

else:
    print(f"{total_coal} pieces of coal left. ({miner_r}, {miner_c})")
