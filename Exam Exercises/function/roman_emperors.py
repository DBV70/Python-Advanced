def list_roman_emperors(*args, **kwargs):
    successful = {}
    unsuccessful = {}
    for arg in args:
        name, success = arg
        if success:
            successful[name] = kwargs[name]
        else:
            unsuccessful[name] = kwargs[name]

    sorted_successful = sorted(successful.items(), key=lambda x: (-x[1], x[0]))
    sorted_unsuccessful = sorted(unsuccessful.items(), key=lambda x: (x[1], x[0]))

    result = f'Total number of emperors: {len(args)}\n'
    if successful:
        result += f'Successful emperors:\n'
        for name, rule in sorted_successful:
            result += f"****{name}: {rule}\n"
    if unsuccessful:
        result += f'Unsuccessful emperors:\n'
        for name, rule in sorted_unsuccessful:
            result += f"****{name}: {rule}\n"

    return result.strip()

# Test code
#print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
#print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
#print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
