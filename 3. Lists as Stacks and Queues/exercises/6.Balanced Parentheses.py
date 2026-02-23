expression = input()
parenthesis = {"(": ")", "[": "]", "{": "}"}
stack = []

for char in expression:
    if char in parenthesis.keys():
        stack.append(char)
    elif char in parenthesis.values():
        if not stack:
            print("NO")
            break
        last_parenthesis = stack.pop()
        if parenthesis[last_parenthesis] != char:
            print("NO")
            break
else:
    print("YES")