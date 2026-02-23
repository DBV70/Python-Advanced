import os
from constants import path_to_dir
path = os.path.join(path_to_dir, "15. File Handling", "exercises")
for_replacement = ["-", ",", ".", "!", "?"]

with open(os.path.join(path, "text.txt")) as file:
    even_lines = [line.rstrip("\n") for lineno, line in enumerate(file, start=0) if lineno % 2 == 0]

output = []
for line in even_lines:
    for char in line:
        if char in for_replacement:
            line = line.replace(char, "@")
    words = list(reversed(line.split()))
    output.append(" ".join(words))

print(*output, sep="\n")
