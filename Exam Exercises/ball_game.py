from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])

goals = 0
while strength and accuracy:
    current_sum = strength[-1] + accuracy[0]
    if current_sum == 100:
        strength.pop()
        accuracy.popleft()
        goals += 1
    elif current_sum < 100:
        if strength[-1] < accuracy[0]:
            strength.pop()
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        else:
            strength[-1] += accuracy[0]
            accuracy.popleft()
    else:
        strength[-1] -= 10
        accuracy.rotate(-1)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals < 1:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals > 0:
    print(f"Goals scored: {goals}")

if strength:
    print("Strength values left: ", end="")
    print(*strength, sep=", ")

if accuracy:
    print("Accuracy values left: ", end="")
    print(*accuracy, sep=", ")