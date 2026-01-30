import os
from constants import path_to_dir
path = os.path.join(path_to_dir, "15. File Handling", "exercises")

def create_file(f_name):
    try:
        file = open(os.path.join(path, f_name), "w")
        file.close()
    except FileExistsError:
        with open(os.path.join(path, f_name), "w") as file:
            file.write("")

def append_to_file(f_name, txt):
    try:
        with open(os.path.join(path, f_name), "a") as file:
            file.write(txt + "\n")
    except FileNotFoundError:
        create_file(f_name)
        append_to_file(f_name, txt)

def replace_text(f_name, old_txt, new_txt):
    try:
        with open(os.path.join(path, f_name), "r") as file:
            txt = file.read()
        with open(os.path.join(path, f_name), "w") as file:
            file.write(txt.replace(old_txt, new_txt))
    except FileNotFoundError:
        print("An error occurred")

def delete_file(f_name):
    try:
        os.remove(os.path.join(path, f_name))
    except FileNotFoundError:
        print("An error occurred")

while True:
    command = input().split('-')
    if command[0] == "End":
        break

    if command[0] == "Create":
        file_name = command[1]
        create_file(file_name)
    elif command[0] == "Add":
        file_name, text = command[1], command[2]
        append_to_file(file_name, text)
    elif command[0] == "Replace":
        file_name, old_text, new_text = command[1], command[2], command[3]
        replace_text(file_name, old_text, new_text)
    elif command[0] == "Delete":
        file_name = command[1]
        delete_file(file_name)
