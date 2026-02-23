def accommodate_new_pets(capacity, max_weight, *args):
    accommodated = {}
    result = []
    for pet, weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight > max_weight:
            continue
        if pet not in accommodated:
            accommodated[pet] = 0
        accommodated[pet] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated.items())]
    return '\n'.join(result)

# Test code
print(accommodate_new_pets(10,15.0,("cat", 5.8), ("dog", 10.0)))
print(accommodate_new_pets(10,10.0,("cat", 5.8), ("dog", 10.5), ("parrot", 0.8), ("cat", 3.1),))
print(accommodate_new_pets(2,15.0,("dog", 10.0), ("cat", 5.8), ("cat", 2.7),))