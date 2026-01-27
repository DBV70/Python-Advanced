from collections import deque

stack = deque()
string = input()

for i, char in enumerate(string):
    if char == "(":
        stack.append(i)
    elif char == ")":
        if stack:
            start_index = stack.pop()
            end_index = i
            print(string[start_index:end_index + 1])
