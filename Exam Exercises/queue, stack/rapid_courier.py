from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())
total_weight = 0

# Accumulates weight of deliverable packages; removes depleted couriers
while packages and couriers:
    # Delivers package if possible; rotates or removes courier
    if packages[-1] <= couriers[0]:
        couriers[0] -= packages[-1] * 2
        total_weight += packages.pop()
        if couriers[0] > 0:
            couriers.rotate(-1)
        else:
            couriers.popleft()
    else:
        packages[-1] -= couriers[0]
        total_weight += couriers[0]
        couriers.popleft()

print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif not packages:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")