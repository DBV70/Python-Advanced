n = int(input())
parking = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        if number not in parking:
            parking.add(number)
    elif direction == "OUT":
        if number in parking:
            parking.remove(number)

if len(parking)== 0:
    print("Parking Lot is Empty")
else:
    for car in parking:
        print(car)
