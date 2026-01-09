from collections import deque

litters = int(input())
people = deque()

command = input()

while command != "Start":
    people.append(command)
    command = input()

while command != "End":
    if command.isdigit():
        person = people.popleft()
        water_needed = int(command)
        if litters >= water_needed:
            litters -= water_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    elif command.startswith("refill"):
        litters += int(command.split()[1])

    command = input()

print(f"{litters} liters left")
