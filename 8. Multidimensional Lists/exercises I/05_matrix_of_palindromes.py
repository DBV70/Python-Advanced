r, c = map(int, input().split())
start = ord('a')

for row in range(r):
    for col in range(c):
        print(f'{chr(row + start)}{chr(row + start + col)}{chr(row + start)}', end=' ')
    print()