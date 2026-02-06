import core
command = input()
sequence = []

while command != "Stop":
    num = int(command.split()[-1])

    if command.startswith('Create'):
        sequence = core.create_sequence(num)
        print(*sequence)
    else:
        if sequence:
            print(core.locate(num, sequence))
        else:
            print(f"Invalid input! Please enter a valid number.")

    command = input()