import os
from constants import path_to_dir
path = os.path.join(path_to_dir, "files", "my_first_file.txt")
with open(path, "w") as file:
    file.write("I just created my first file!")

