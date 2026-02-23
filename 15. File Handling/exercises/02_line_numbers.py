import os
from constants import path_to_dir
path = os.path.join(path_to_dir, "15. File Handling", "exercises")
letters = 0
specials = 0

output = open(os.path.join(path, "output.txt"), "w")
output.write("")

with open(os.path.join(path, "text.txt")) as file:
    for lineno, line in enumerate(file, start=1):
        letters = len([ch for ch in line if ch.isalpha()])
        specials = len([ch for ch in line if ch in ".,':;!?-"])
        line = f"Line {lineno}: " + line.rstrip("\n") + f" ({letters})({specials})"
        # with open(os.path.join(path, "output.txt"), "a") as output:
        output.write(line + "\n")

output.close()