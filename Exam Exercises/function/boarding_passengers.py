def boarding_passengers(capacity:int, *args):
    boarded = {}
    waiting = False

    for passengers, group in args[0:]:
        if capacity >= passengers:
            if group not in boarded:
                boarded[group] = 0
            capacity -= passengers
            boarded[group] += passengers
        else:
            waiting = True
            if capacity <= 0:
                break

    sorted_boarded = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))
    result = ["Boarding details by benefit plan:"]
    for group, passengers in sorted_boarded:
        result.append(f"## {group}: {passengers} guests")

    if not waiting:
        result.append("All passengers are successfully boarded!")
    elif capacity <= 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)

# test code
print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
