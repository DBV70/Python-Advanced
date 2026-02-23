from collections import deque
reverse_string = deque()

string = input()
for char in string:
    reverse_string.appendleft(char)

print(''.join(reverse_string))