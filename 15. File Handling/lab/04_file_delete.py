import os
from constants import path_to_dir

path = os.path.join(path_to_dir, "files", "to_delete.txt" )

try:
    os.remove((path))
except FileNotFoundError:
    print("File already deleted!")