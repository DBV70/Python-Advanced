from collections import deque

initial_fuel = [int(x) for x in input().split()]
indexes = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

reached = []
i = 0
while initial_fuel and indexes:
    i += 1
    fuel = initial_fuel.pop()
    index = indexes.popleft()
    difference = fuel - index
    if difference >= fuel_needed[0]:
        fuel_needed.popleft()
        reached.append(i)
        print(f"John has reached: Altitude {i}")
        continue
    print(f"John did not reach: Altitude {i}")
    break

if reached:
    if indexes:
        print("John failed to reach the top.")
        print(f"Reached altitudes: {', '.join([f"Altitude {str(i)}" for i in reached])}")
    else:
        print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John did not reach the top.")
    print("John didn't reach any altitude.")
