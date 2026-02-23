from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()
    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)
    else:
        pie -= contestant
        if pie == 1 and pies:
            pies[-1] += 1
        else:
            pies.append(pie)

if not contestants and not pies:
    print("We have a champion!")
elif contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")
else:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")