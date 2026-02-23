from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

# Simulates battle until one side is depleted
while bees and bee_eaters:
    defenders = bees.popleft()
    attackers = bee_eaters.pop()

    while attackers > 0 and defenders >= 7:
        defenders -= 7
        attackers -= 1

    if defenders < 7:
        bee_eaters.append(attackers) if attackers > 0 else None
    if attackers == 0:
        bees.append(defenders) if defenders > 0 else None

print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(str(b) for b in bees)}")
else:
    print(f"Bee-eater groups left: {', '.join(str(be) for be in bee_eaters)}")
