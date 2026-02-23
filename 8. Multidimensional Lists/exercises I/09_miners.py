field_size = int(input())
commands = input().split()
field = []
miner_r, miner_c = 0, 0
total_coal = 0

moves = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for row in range(field_size):
    field.append(input().split())
    if 's' in field[row]:
        miner_r, miner_c = row, field[row].index('s')
    total_coal += field[row].count('c')

for command in commands:
    new_r, new_c = moves[command](miner_r, miner_c)
    if 0 <= new_r < field_size and 0 <= new_c < field_size:
        miner_r, miner_c = new_r, new_c
        if field[new_r][new_c] == 'e':
            print(f"Game over! ({new_r}, {new_c})")
            exit()
        elif field[new_r][new_c] == 'c':
            total_coal -= 1
            field[new_r][new_c] = '*'
            if total_coal == 0:
                print(f"You collected all coal! ({new_r}, {new_c})")
                exit()

print(f"{total_coal} pieces of coal left. ({miner_r}, {miner_c})")
