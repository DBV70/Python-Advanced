from collections import deque

def solve_crossroads():
    green_light_duration = int(input())
    free_window_duration = int(input())

    cars_queue = deque()
    total_cars_passed = 0

    while True:
        command = input()

        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break

        if command == "green":
            current_green = green_light_duration

            while current_green > 0 and cars_queue:
                car = cars_queue.popleft()
                car_length = len(car)

                # Case 1: Car passes completely during the green light
                if current_green >= car_length:
                    current_green -= car_length
                    total_cars_passed += 1
                else:
                    # Case 2: Car uses the rest of the green light and needs the free window
                    remaining_car_part = car_length - current_green

                    if remaining_car_part <= free_window_duration:
                        # Car passes during the free window
                        total_cars_passed += 1
                    else:
                        # Crash!
                        # The character hit is at the index: green light + free window
                        hit_index = current_green + free_window_duration
                        print("A crash happened!")
                        print(f"{car} was hit at {car[hit_index]}.")
                        return

                    current_green = 0
        else:
            # It's a car model, add to queue
            cars_queue.append(command)


if __name__ == "__main__":
    solve_crossroads()
