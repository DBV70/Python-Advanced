from collections import deque

def solve_cups_and_bottles():
    # Cups: First entered, first filled (Queue)
    cups = deque(map(int, input().split()))
    # Bottles: Last entered, first picked (Stack)
    bottles = list(map(int, input().split()))

    wasted_water = 0

    while cups and bottles:
        current_cup = cups.popleft()

        while current_cup > 0 and bottles:
            current_bottle = bottles.pop()

            if current_bottle >= current_cup:
                # Cup is filled, calculate wasted water
                wasted_water += (current_bottle - current_cup)
                current_cup = 0
            else:
                # Cup is not full yet, reduce its remaining capacity
                current_cup -= current_bottle

    if not cups:
        # All cups are filled
        remaining_bottles = " ".join(map(str, bottles[::-1]))
        print(f"Bottles: {remaining_bottles}")
    else:
        # Bottles ran out
        remaining_cups = " ".join(map(str, cups))
        print(f"Cups: {remaining_cups}")

    print(f"Wasted litters of water: {wasted_water}")

if __name__ == "__main__":
    solve_cups_and_bottles()