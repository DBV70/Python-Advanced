def accommodate(*args, **kwargs):
    guests = list(args)
    rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0][5:]))
    accommodated = {}
    accommodations = 0
    unaccommodated = 0

    while guests and rooms:
        for room in rooms:
            room_no, capacity = room[0][5:], room[1]
            if room_no not in accommodated and capacity >= guests[0]:
                accommodated[room_no] = guests[0]
                accommodations += 1
                rooms.remove(room)
                break
        else:
            unaccommodated += guests[0]
        guests.remove(guests[0])

    sorted_accommodated = sorted(accommodated.items(), key=lambda x: int(x[0]))
    result = []

    if not accommodated:
        result.append("No accommodations were completed!")
    else:
        result.append(f"A total of {accommodations} accommodations were completed!")
        for room, guests in sorted_accommodated:
            result.append(f"<Room {room} accommodates {guests} guests>")

    if unaccommodated:
        result.append(f"Guests with no accommodation: {unaccommodated}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return '\n'.join(result)

# test code
# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))