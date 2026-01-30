import os
from constants import path_to_dir
path = os.path.join(path_to_dir, "15. File Handling", "exercises")

report = {}
files = os.listdir(path)
for file in files:
    extension = file.split(".")[-1]
    if extension not in report:
        report[extension] = []
    report[extension].append(file)

with open(os.path.join(path, "report.txt"), "w") as file:
    file.write("")

with open(os.path.join(path, "report.txt"), "a") as file:
    for extension, files in sorted(report.items(), key=lambda x: (x[0])):
        file.write(f".{extension}\n")
        for f in sorted(files):
            file.write (f"---{f}\n")
