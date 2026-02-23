from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

matches = 0
worms_count = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    if worm == hole:
        matches += 1
        continue
    else:
        worm -= 3
        if worm <= 0:
            continue
        worms.append(worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == worms_count:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
else:
    print("Holes left: none")

